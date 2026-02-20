import csv

# Assumes dati.csv exists. If not, run 01_write_basic_writer.py first.
with open("dati.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    headers = next(reader)  # skip header row
    print("Headers:", headers)

    for row in reader:
        name = row[0]
        age_text = row[1]
        age = int(age_text)  # type conversion
        print(f"{name} is {age} years old")
