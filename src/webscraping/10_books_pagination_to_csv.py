"""10_books_pagination_to_csv.py
Pilnāks piemērs:
- ielādē vairākas books.toscrape.com lapas (pagination)
- izvelk grāmatu nosaukumus un cenas
- saglabā rezultātu CSV failā

Piemērs ir "pieklājīgs": izmanto User-Agent un pauzes.
"""

import csv
import time
from dataclasses import dataclass
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE = "http://books.toscrape.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0 Safari/537.36"
}


@dataclass
class Book:
    title: str
    price: str
    relative_url: str

    @property
    def absolute_url(self) -> str:
        return urljoin(BASE, self.relative_url)


def parse_page(html: bytes) -> List[Book]:
    soup = BeautifulSoup(html, "html.parser")
    books: List[Book] = []

    # Katra grāmata ir <article class="product_pod">
    for art in soup.find_all("article", class_="product_pod"):
        a = art.find("h3").find("a") if art.find("h3") else None
        price_tag = art.find("p", class_="price_color")

        if not a or not price_tag:
            continue

        title = (a.get("title") or a.text or "").strip()
        rel = (a.get("href") or "").strip()
        price = price_tag.text.strip()

        if title and rel and price:
            books.append(Book(title=title, price=price, relative_url=rel))

    return books


def main() -> None:
    # Cik lapas vēlamies noskrāpēt (books.toscrape.com kopā ir 50, bet te pietiek ar dažām)
    max_pages = 5
    all_books: List[Book] = []

    for page_num in range(1, max_pages + 1):
        url = urljoin(BASE, f"catalogue/page-{page_num}.html")
        print(f"[{page_num}/{max_pages}] Ielādēju: {url}")

        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code != 200:
            print("  Neizdevās ielādēt lapu. Statuss:", r.status_code)
            break

        page_books = parse_page(r.content)
        print("  Atrasts grāmatu skaits:", len(page_books))
        all_books.extend(page_books)

        time.sleep(1)  # pieklājīga pauze

    out_csv = "books_sample.csv"
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        wtr = csv.writer(f)
        wtr.writerow(["title", "price", "url"])
        for b in all_books:
            wtr.writerow([b.title, b.price, b.absolute_url])

    print("Saglabāts:", out_csv)
    print("Kopā grāmatu:", len(all_books))


if __name__ == "__main__":
    main()
