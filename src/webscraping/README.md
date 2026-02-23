# Web Scraping (rasmošana) ar `requests` + `BeautifulSoup4` (Python)

Šajā mapē ir nelieli, praktiski `.py` piemēri, kas atbilst prezentācijā aplūkotajām tēmām:  
- kas ir web scraping un kā tas tehniski strādā (Request → Parse → Extract)  
- `requests` pamatlietošana un statusa kodi  
- `BeautifulSoup4` pamatlietošana: `find()`, `find_all()`, meklēšana pēc `id` un `class_`  
- atribūtu (`href`, `src`) iegūšana  
- labākās prakses: `User-Agent`, pauzes (`time.sleep`), kļūdu apstrāde (`try/except`)  
- praktisks piemērs ar **https://books.toscrape.com/**

> **Piezīme par ētiku un likumību:** vienmēr pārbaudi vietnes `robots.txt` un lietošanas noteikumus (Terms of Service).  
> Nepārslogo serveri — ievēro pauzes starp pieprasījumiem.

---

## Prasības

- Python 3.10+ (der arī 3.8+)
- Bibliotēkas:
  - `requests`
  - `beautifulsoup4`

Instalācija:

```bash
pip install -r requirements.txt
```

---

## Kā palaist piemērus

No šīs mapes:

```bash
python 01_requests_basic.py
python 05_books_toscrape_h1.py
python 10_books_pagination_to_csv.py
```

---

## Failu saraksts

- `01_requests_basic.py` — vienkāršs GET pieprasījums ar `requests`
- `02_response_status.py` — statusa kodu pārbaude + HTML fragmenta izdruka
- `03_bs4_title.py` — `BeautifulSoup` “soup” izveide un `<title>` nolasīšana
- `04_find_findall.py` — `find()` un `find_all()` piemēri
- `05_books_toscrape_h1.py` — praktisks “hello world” skrāpis: virsraksts no books.toscrape.com
- `06_extract_links_generic.py` — linku (`<a>`) teksta un `href` iegūšana
- `07_user_agent.py` — pieprasījums ar `User-Agent` galveni
- `08_polite_sleep_loop.py` — pieprasījumu cikls ar pauzēm
- `09_try_except.py` — kļūdu apstrādes šablons
- `10_books_pagination_to_csv.py` — vairākas lapas (pagination) + grāmatu nosaukumi/cenas + saglabāšana CSV

---

## Tipiskas problēmas

- **403 Forbidden**: bieži palīdz `User-Agent` galvene (skat. `07_user_agent.py`).
- **HTML struktūra mainās**: jāpielāgo selektori (`class_`, `id`, tagu struktūra).
- **Lapas ir dinamiskas (JS)**: `requests`/`bs4` var nebūt pietiekami; tad vajag Selenium/Playwright.

Lai veicas!
