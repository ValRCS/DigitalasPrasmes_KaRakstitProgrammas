import csv

speeds = []

with open("kustiba_merijumi.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        time_s = float(row["time_s"])
        distance_m = float(row["distance_m"])

        if time_s <= 0:
            raise ValueError(f"Invalid time_s={time_s}. Must be > 0.")

        speed = distance_m / time_s
        speeds.append(speed)

        print(f"Ātrums: {speed:.2f} m/s")

if speeds:
    avg_speed = sum(speeds) / len(speeds)
    print(f"Vidējais ātrums: {avg_speed:.2f} m/s")
else:
    print("Nav datu.")
