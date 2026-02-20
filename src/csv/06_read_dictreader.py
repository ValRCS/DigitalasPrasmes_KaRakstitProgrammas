import csv

# Assumes dati2.csv exists. If not, run 02_write_writerows.py first.
with open("dati2.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";") # DictReader automātiski nolasa pirmo rindu kā galveni (header) un katru nākamo rindu pārvērš par vārdnīcu, kur atslēgas ir galvenes nosaukumi
    for row in reader:
        # tātad mums ir jāzin ka CSV datnē ir "name" un "age" lauki, lai varētu tos izmantot kā atslēgas vārdnīcā
        name = row["name"]
        age = int(row["age"])  # CSV values are strings
        # ja nezinam vai kolonna būs tad lietojam get metodi, kas ļauj norādīt noklusējuma vērtību, ja atslēga nav atrasta
        # mums ir ekstra_kolonna, kas nav obligāta, tāpēc varam izmantot get metodi ar noklusējuma vērtību None
        extra = row.get("ekstra_kolonna", None)
        if extra is None:
            extra = "nav papildu informācijas"
        print(f"{name}: {age}, ekstra: {extra}")

