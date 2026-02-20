import csv

rows = [
    ["name", "age"],
    ["Jānis", 25],
    ["Anna", 30],
    ["Pēteris", 28],
]

with open("dati.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(rows)

print("Saved dati.csv")
