"""02_response_status.py
Atbildes objekts: .status_code un .text (HTML kā teksts).
"""

import requests

def main() -> None:
    url = "https://example.com"
    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        print("Lapa ielādēta veiksmīgi!")
        # Izdrukājam pirmos 200 simbolus, lai redzētu, ka tiešām saņēmām HTML
        print(response.text[:200])
    else:
        print("Kļūda! Statuss:", response.status_code)

if __name__ == "__main__":
    main()
