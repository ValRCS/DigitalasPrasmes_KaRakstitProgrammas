"""01_requests_basic.py
Vienkāršākais piemērs: nosūtām GET pieprasījumu un izdrukājam statusa kodu.
"""

import requests

def main() -> None:
    url = "https://www.google.com"
    response = requests.get(url, timeout=15)
    print("Pieprasījums nosūtīts!")
    print("Statuss:", response.status_code)

if __name__ == "__main__":
    main()
