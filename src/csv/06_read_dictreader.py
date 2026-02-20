import csv

# Assumes dati2.csv exists. If not, run 02_write_writerows.py first.
with open("dati2.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        name = row["name"]
        age = int(row["age"])  # CSV values are strings
        print(f"{name}: {age}")
