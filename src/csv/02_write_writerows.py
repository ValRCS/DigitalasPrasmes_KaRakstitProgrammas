import csv

data_rows = [
    ["Jānis", 25],
    ["Anna", 30],
    ["Pēteris", 28],
]

with open("dati2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["name", "age"])   # headers
    writer.writerows(data_rows)        # all data rows at once

print("Saved dati2.csv")
