"""04_find_findall.py
Demonstrē find() un find_all() pamatlietošanu.
"""

import requests
from bs4 import BeautifulSoup

def main() -> None:
    url = "https://example.com"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # find() — pirmais elements
    h1 = soup.find("h1")
    if h1:
        print("Pirmais <h1>:", h1.text.strip())
    else:
        print("Nav atrasts neviens <h1>.")

    # find_all() — visi elementi
    links = soup.find_all("a")
    print(f"Atrastās saites: {len(links)}")
    for i, a in enumerate(links[:10], start=1):
        print(f"{i:02d}.", a.text.strip() or "(tukšs teksts)")

if __name__ == "__main__":
    main()
