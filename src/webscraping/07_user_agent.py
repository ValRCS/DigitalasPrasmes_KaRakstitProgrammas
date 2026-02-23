"""07_user_agent.py
Daudzas lapas bloķē skriptus. Norādām User-Agent, lai izliktos par pārlūku.
"""

import requests

def main() -> None:
    url = "http://books.toscrape.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=15)
    print("Statuss:", response.status_code)
    print(response.text[:200])

if __name__ == "__main__":
    main()
