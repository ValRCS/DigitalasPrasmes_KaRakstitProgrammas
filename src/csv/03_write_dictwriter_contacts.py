import csv

# sagatavosim sarakstu ar kontaktu datiem, kur katrs kontakts ir vārdnīca (dictionary)
contacts = [
    {"name": "Jānis", "email": "janis@example.com"},
    {"name": "Anna", "email": "anna@site.lv","telephone":"12345678"},
]

fieldnames = ["name", "telephone", "email"] # šis saraksts nosaka, kādi lauki tiks ierakstīti CSV datnē un kādā secībā

with open("kontakti.csv", "w", encoding="utf-8", newline="") as f:
    # padodam laukumu nosaukumus (fieldnames) un atdalītāju ";"
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(contacts)
# atkal fails jau šeit ir automātiski aizvērts, jo izmantojām "with" konteksta pārvaldnieku

print("Saved kontakti.csv")
