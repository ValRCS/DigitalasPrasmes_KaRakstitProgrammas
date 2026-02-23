"""08_polite_sleep_loop.py
Pieprasījumu cikls ar pauzēm, lai nepārslogotu serveri.
"""

import time
import requests

def main() -> None:
    pages = [
        "http://books.toscrape.com/catalogue/page-1.html",
        "http://books.toscrape.com/catalogue/page-2.html",
        "http://books.toscrape.com/catalogue/page-3.html",
    ]

    for url in pages:
        print("Ielādēju:", url)
        r = requests.get(url, timeout=15)
        print("  Statuss:", r.status_code)
        time.sleep(2)  # 2 sekunžu pauze starp pieprasījumiem

if __name__ == "__main__":
    main()
