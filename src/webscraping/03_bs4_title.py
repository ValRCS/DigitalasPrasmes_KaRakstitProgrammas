"""03_bs4_title.py
BeautifulSoup "soup" izveide un <title> elementa nolasīšana.
"""

import requests
from bs4 import BeautifulSoup

def main() -> None:
    url = "https://example.com"
    response = requests.get(url, timeout=15)
    # raise_for_status() izmet kļūdu, ja statuss nav 200-299
    response.raise_for_status() # tā ir alternatīva status_code pārbaudei ar if

    # parsējam HTML un izvelkam <title> tekstu
    soup = BeautifulSoup(response.content, "html.parser")
    # soup.title var būt None, ja lapā nav <title>
    title_text = soup.title.text.strip() if soup.title else "(nav <title>)"
    print("Lapas title:", title_text)

if __name__ == "__main__":
    main()
