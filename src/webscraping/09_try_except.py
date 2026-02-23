"""09_try_except.py
Internets nav stabils. Try/except šablons, lai skripts neapstātos pie pirmās kļūdas.
"""

import requests

def main() -> None:
    url = "http://books.toscrape.com/"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        print("OK:", response.status_code)
    except requests.RequestException as e:
        print(f"Kļūda pieprasījumā: {e}")

if __name__ == "__main__":
    main()
