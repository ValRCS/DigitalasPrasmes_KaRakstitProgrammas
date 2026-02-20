import csv

# Demonstrates how to deal with accidental whitespace in CSV headers.
with open("kustiba_merijumi_with_spaces.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")

    # Normalize fieldnames (strip whitespace)
    if reader.fieldnames:
        reader.fieldnames = [h.strip() for h in reader.fieldnames]

    for row in reader:
        # Normalize keys too (extra defensive)
        row = {k.strip(): v.strip() for k, v in row.items()}

        try:
            time_s = float(row["time_s"])
            distance_m = float(row["distance_m"])
        except KeyError as e:
            print(f"Missing column in CSV: {e}")
            continue
        except ValueError as e:
            print(f"Invalid data format: {e}")
            continue

        if time_s <= 0:
            print(f"Invalid time_s={time_s}. Must be > 0.")
            continue

        speed = distance_m / time_s
        print(f"Ātrums: {speed:.2f} m/s")

# aprēķinam vidējo ātrumu, ja ir dati
# TODO aprēķiniet paši ieliekot saraksta un tad aprēķinot vidējo vērtību, ja saraksts nav tukšs. Ja saraksts ir tukšs, tad izdrukājiet "Nav datu."
