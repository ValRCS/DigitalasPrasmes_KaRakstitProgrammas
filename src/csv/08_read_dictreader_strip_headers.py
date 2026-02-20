import csv

# Demonstrates how to deal with accidental whitespace in CSV headers.
with open("kustiba_merijumi_with_spaces.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")

    # Normalize fieldnames (strip whitespace)
    if reader.fieldnames:
        reader.fieldnames = [h.strip() for h in reader.fieldnames]

    for row in reader:
        # Normalize keys too (extra defensive)
        row = {k.strip(): v for k, v in row.items()}

        time_s = float(row["time_s"])
        distance_m = float(row["distance_m"])

        speed = distance_m / time_s
        print(f"Ātrums: {speed:.2f} m/s")
