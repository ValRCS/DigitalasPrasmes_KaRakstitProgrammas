"""06_extract_links_generic.py
Atribūtu iegūšana: href. Parāda kā strādāt ar <a> tagiem.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main() -> None:
    base_url = "https://example.com"
    response = requests.get(base_url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    for a in links[:20]:
        text = a.text.strip() or "(tukšs teksts)"
        href = a.get("href")  # drošāk nekā a["href"], jo var nebūt
        if not href:
            continue
        absolute = urljoin(base_url, href)
        print(text)
        print("  href:", href)
        print("  absolute:", absolute)
        print("---")

if __name__ == "__main__":
    main()
