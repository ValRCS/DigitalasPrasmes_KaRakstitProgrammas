import csv # iebūvēta Python bibliotēka darbam ar CSV datnēm

# izveidojam sarakstu ar datiem, ko vēlamies ierakstīt CSV datnē
rows = [
    ["name", "age"], # galvene (header) ar kolonnu nosaukumiem
    ["Jānis", 25],
    ["Anna", 30],
    ["Pēteris", 28],
]

# atverat teksta failu rakstīšanas režīmā ("w"), norādot kodējumu un jaunas rindas simbolu
with open("dati.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")  #ievērojam atdalītāju ";", nevis noklusēto ","
    writer.writerows(rows)
# šeit fails jau ir automātiski aizvērts, jo izmantojām "with" konteksta pārvaldnieku

print("Saved dati.csv")
