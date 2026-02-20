import csv

# Assumes dati.csv exists. If not, run 01_write_basic_writer.py first.
with open("dati.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)
