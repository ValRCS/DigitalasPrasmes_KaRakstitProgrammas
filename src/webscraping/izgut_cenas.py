# Apgūstam tīmekļa rasmošanu / skrāpēšanu, izmantojot BeautifulSoup un Requests bibliotēkas

# Sākam ar mērķi: iegūt informāciju par grāmatām no pirmās lapas: https://books.toscrape.com/
# mēs gribēsim iegūt grāmatu nosaukumus, cenas, piejamību un vērtējumu
# pēc tam saglabāt šo informāciju CSV failā kur viena rindiņa atbilst vienai grāmatai

# Izpēte: mums ir jāpizpēta tīmekļa lapa, lai saprastu tās struktūru un atrastu elementus, kurus vēlamies iegūt
# mēs varam izmantot pārlūkprogrammas izstrādātāja rīkus, lai apskatītu HTML struktūru un atrastu nepieciešamos elementus
# piemēram, grāmatu nosaukumi atrodas <h3> elementā

# izpētes rezultātā redzam 
# ka katra grāmata ir ietverta <article class="product_pod"> elementā
# ar to varētu sākt un atrast visus šo elementus, lai iegūtu nepieciešamo informāciju

# tad sākam ar moduļu importēšanu
# parasti importējam iebūvētos moduļus vispirms, pēc tam trešo pušu bibliotēkas, un visbeidzot mūsu pašu moduļus
import csv # iebūvēts bibliotēkas modulis, kas ļauj mums strādāt ar CSV failiem

try:
    import requests
except ImportError:
    print("requests bibliotēka nav instalēta")
    print("Uzstādiet to no komandrindas: pip install requests")
    exit(1) # beidzam programmu ar kļūdas kodu 1

try:
    from bs4 import BeautifulSoup # bibliotēka, kas ļauj mums analizēt un izvilkt datus no HTML dokumentiem
except ImportError:
    print("BeautifulSoup bibliotēka nav instalēta")
    print("Uzstādiet to no komandrindas: pip install beautifulsoup4")
    exit(1) # beidzam programmu ar kļūdas kodu 1

url = 'http://books.toscrape.com/' # mērķa tīmekļa lapas URL
print(f"Iegūstam datus no: {url}")

# tagad iegūstam lapas saturu, izmantojot requests.get() funkciju
response = requests.get(url) # nosūtām GET pieprasījumu uz norādīto URL
# pārbaudām, vai pieprasījums bija veiksmīgs (statusa kods 200)
if response.status_code == 200:
    print("Lapa veiksmīgi iegūta")
    # tagad mums ir HTML saturs, ko varam analizēt ar BeautifulSoup
else:
    print(f"Neizdevās iegūt lapu, statusa kods: {response.status_code}")
    exit(1) # beidzam programmu ar kļūdas kodu 1

# te mēs zinam ka lapa ir veiksmīgi iegūta, tāpēc varam turpināt ar BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser') # izveidojam BeautifulSoup objektu, lai analizētu HTML saturu
# izdrukājam lapas nosaukumu, lai pārliecinātos, ka esam pareizajā lapā
print(f"Lapas nosaukums: {soup.title.string}")

# iegūsim sarakstu ar visām grāmatām, kas atrodas <article class="product_pod"> elementā
books = soup.find_all('article', class_='product_pod') # atrodam visus <article> elementus ar klasi "product_pod"
# ievērojiet ka class_ ir jānorāda ar apakšsvītru, jo class ir rezervēts vārds Pythonā
print(f"Grāmatu skaits lapā: {len(books)}")

# es varētu validēt šeit ar assert ka grāmatu skaits ir 20, jo lapā ir 20 grāmatas
assert len(books) == 20, "Grāmatu skaits nav 20, kā gaidīts"
# ja būs kļuda, tad programma apstāsies un izdrukās šo kļūdas ziņojumu
# šeit zinam ka viss ir kārtībā, tāpēc varam turpināt ar datu izvilkšanu

# izdrukāsim pirmās grāmatas informāciju, lai redzētu, kā izskatās dati
first_book = books[0] # iegūstam pirmo grāmatu no saraksta
# izdrukāsim visu pirmās grāmatas HTML struktūru, lai redzētu, kā izskatās dati
print(first_book.prettify()) # izdrukājam pirmās grāmatas HTML struktūru, lai redzētu, kā izskatās dati

# gŗāmatas nosaukums atrodas h3 - tehniski zem enkura <a> elementa, tāpēc varam izmantot find() metodi, lai to atrastu
book_title = first_book.find('h3').find('a')['title'] # atrodam grāmatas nosaukumu, izmantojot find() metodi un piekļūstot title atribūtam
# tikai jāņem vēra ka find var arī atgriezt None, ja elements netiek atrasts, tāpēc būtu labi pārbaudīt vai elements ir atrasts pirms piekļūstam tā atribūtam
print(f"Grāmatas nosaukums: {book_title}")
# otrs veids kā iegūt nosaukumu paņemam tekstu no h3 elementa, bet tas var būt mazāk precīzs, jo var būt lieki atstarpes vai citi teksta elementi
also_book_title = first_book.find('h3').get_text(strip=True) # iegūt tekstu no h3 elementa, izmantojot get_text() metodi ar strip=True, lai noņemtu liekas atstarpes
print(f"Grāmatas nosaukums (ar strip=True): {also_book_title}")

# meklēsim tagad cenu tā ir mūsu article elementa iekšā <p class="price_color"> elementā
# book_price = first_book.find('p', class_='price_color').get_text() # atrodam grāmatas cenu, izmantojot find() metodi un piekļūstot tekstam
# mēs varam arī padot vārdnīcu ar klasi, lai atrastu elementu, kas atbilst noteiktai klasei
book_price = first_book.find('p', {'class': 'price_color'}).get_text() # atrodam grāmatas cenu, izmantojot find() metodi un piekļūstot tekstam
# šī metode ir elastīgāka, jo ļauj mums meklēt elementus, kas atbilst noteiktai klasei, pat ja klasei ir vairākas vērtības
# un varam vārdnīca padot vairākus atribūtus, lai atrastu elementu, kas atbilst visiem šiem atribūtiem
print(f"Grāmatas cena: {book_price}")
# attīram cenu mums interesē tikai cena pēc simbols £, tāpēc varam izmantot str.replace() metodi, lai noņemtu šo simbolu
# clean_price = book_price.replace('£', '') # noņemam £ simbolu no cenas
# vēl drošak būtu dalīt cenu un simbolu, izmantojot str.partition() metodi, kas atgriež trīs daļas: pirms simbols, simbols un pēc simbols
# izmantojam split() metodi, lai sadalītu cenu un simbolu, un iegūstam tikai cenu daļu
clean_price = book_price.split('£')[-1] # sadalām cenu un simbolu un ņemam pēdejo daļu, kas ir cena
# šis strādās pat ja nav mārciņas simbols, jo mēs ņemam pēdejo daļu pēc sadalīšanas
print(f"Attīrīta cena: {clean_price}")
# pārvēršam cenu par skaitli, lai varētu veikt aprēķinus, izmantojot float() funkciju
numeric_price = float(clean_price) # pārvēršam cenu par skaitli, lai varētu veikt aprēķinus, izmantojot float() funkciju
print(f"Skaitliskā cena: {numeric_price}")
# ja gribam tikai glabāt šis nebija nepieciešams, bet tas var būt noderīgi, ja vēlamies veikt aprēķinus ar cenām

# visbeidzot apskatījam piejamību, kas atrodas <p class="instock availability"> elementā
availability = first_book.find('p', class_='instock availability')
# ja neatrodam tad False ja atradām tad True
is_available = True # pieņemam, ka grāmata ir pieejama
if availability is None: # ja neatrodam piejamības elementu, tad pieņemam, ka grāmata nav pieejama
    is_available = False
# vaŗeja to darīt īsāk bet šis ir skaidrāks un vieglāk saprotams, jo mēs pārbaudām vai elements ir atrasts, nevis meklējam konkrētu tekstu elementā, kas var būt mazāk precīzs
if availability:
    print("Grāmata ir pieejama")

# uzrakstam funkciju kurai padot article elementu un atgriež vārdnīcu ar grāmatas informāciju
def extract_book_info(book):
    """Izgūst grāmatas informāciju no article elementa un atgriež vārdnīcu ar šo informāciju"""
    book_title = book.find('h3').find('a')['title'] # iegūstam grāmatas nosaukumu
    book_price = book.find('p', {'class': 'price_color'}).get_text() # iegūstam grāmatas cenu
    clean_price = book_price.split('£')[-1] # attīram cenu, noņemot £ simbolu
    numeric_price = float(clean_price) # pārvēršam cenu par skaitli
    availability = book.find('p', class_='instock availability') # iegūstam piejamības elementu
    is_available = True # pieņemam, ka grāmata ir pieejama
    if availability is None: # ja neatrodam piejamības elementu, tad pieņemam, ka grāmata nav pieejama
        is_available = False
    # atgriežu jaunu vārdnīcu ar grāmatas informāciju
    return {
        'title': book_title,
        'price': numeric_price,
        'available': is_available
    }

# pārbaudam ar pirmo un otro grāmatu, lai pārliecinātos, ka funkcija strādā pareizi
first_book_info = extract_book_info(books[0]) # iegūstam pirmās grāmatas informāciju, izmantojot funkciju
print(f"Pirmās grāmatas informācija: {first_book_info}")
second_book_info = extract_book_info(books[1]) # iegūstam otrās grāmatas informāciju, izmantojot funkciju
print(f"Otrās grāmatas informācija: {second_book_info}")

# uzrakstam tagad funkciju kurai padot sarakstu ar article elementiem un atgriež sarakstu ar vārdnīcām, kur katra vārdnīca satur grāmatas informāciju
def extract_books_info(books):
    """Izgūst grāmatu informāciju no saraksta ar article elementiem un atgriež sarakstu ar vārdnīcām, kur katra vārdnīca satur grāmatas informāciju"""
    books_info = [] # izveidojam tukšu sarakstu, kur glabāsim grāmatu informāciju
    for book in books: # iterējam cauri visām grāmatām
        book_info = extract_book_info(book) # iegūstam grāmatas informāciju, izmantojot iepriekš definēto funkciju
        books_info.append(book_info) # pievienojam grāmatas informāciju sarakstam
    return books_info # atgriežam sarakstu ar grāmatu informāciju

books_info = extract_books_info(books) # iegūstam visu grāmatu informāciju, izmantojot funkciju
# tātad books_info ir saraksts ar vārdnīcām, kur katra vārdnīca satur grāmatas informāciju
print(f"Visu grāmatu informācija: {books_info}")

# tagad varam saglabāt csv failā ar csv DictionerWriter klasi, kas ļauj mums rakstīt vārdnīcas CSV formātā
csv_file = 'books_info.csv' # nosaukums CSV failam, kurā saglabāsim grāmatu informāciju
with open(csv_file, mode='w', newline='', encoding='utf-8') as file: # atveram CSV failu rakstīšanas režīmā ar UTF-8 kodējumu
    fieldnames = ['title', 'price', 'available'] # definējam lauku nosaukumus, kas atbilst vārdnīcas atslēgām
    writer = csv.DictWriter(file, fieldnames=fieldnames) # izveidojam DictWriter objektu, lai rakstītu vārdnīcas CSV formātā
    writer.writeheader() # rakstām CSV galveni ar lauku nosaukumiem
    for book_info in books_info: # iterējam cauri visām grāmatu informācijām pa vienai
        writer.writerow(book_info) # rakstām katru grāmatas informāciju kā rindu CSV failā

print(f"Grāmatu informācija ir saglabāta failā: {csv_file}")

# TODO iegūt adresi konkrētai grāmatai kā jaunu lauku un arī saglabāt to CSV failā


# TODO izveidot sarakstu ar url adresēm visām grāmatām un saglabāt to atsevišķā CSV failā, kur katra rindiņa atbilst vienai grāmatai un satur tikai tās URL adresi
# jo ja mēs mākam apstrādat vienu lapu kādai vietnei
# tad liela varbūtība, ka mēs spēsim līdzīgas lapas apstrādāt tāpat, tikai mainot URL adresi

# silts ieteikums: ja mēs gribam iegūt informāciju no vairākām lapām, piemēram, no visām lapām vietnē, kur ir vairākas lapas ar grāmatām, tad mums būs jāizveido cikls, kas iterē cauri visām lapām un iegūst informāciju no katras lapas
# labā prakse būs ka liksim time.sleep(1) funkciju, lai ievietotu pauzi starp pieprasījumiem, lai neuzspiestu pārāk lielu slodzi uz serveri un izvairītos no bloķēšanas