"""05_books_toscrape_h1.py
Praktisks piemērs no prezentācijas: paņemam lapu un izvadām <h1>.
Avots: http://books.toscrape.com/
"""

import requests
from bs4 import BeautifulSoup

def main() -> None:
    url = "http://books.toscrape.com/"
    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1")
        if title:
            print(f"Lapas virsraksts: {title.text.strip()}")
        else:
            print("Neizdevās atrast <h1>.")
    else:
        print("Kļūda ielādējot lapu. Statuss:", response.status_code)

if __name__ == "__main__":
    main()
