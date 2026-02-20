import csv

speeds = []

with open("kustiba_merijumi.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter=";")

    # iterējam cauri katrai rindiņai CSV datnē, un katra rindiņa ir vārdnīca (dictionary), kur atslēgas ir kolonnu nosaukumi no galvenes (header)
    for row in reader:
        # atkal jāzin kuras kolonnas ir CSV datnē, lai varētu tās izmantot kā atslēgas vārdnīcā
        # ja sagaidāms ka kaut kur būs kļūda, tad var izmantot try-except bloku, lai apstrādātu izņēmumus, piemēram, ja kāda kolonna nav atrasta (KeyError) vai ja dati nav pareizā formātā (ValueError)
        try:
            time_s = float(row["time_s"])
            distance_m = float(row["distance_m"])
        except KeyError as e:
            print(f"Missing column in CSV: {e}")
            continue # turpinam ar nākamo rindu, ja trūkst kāda kolonna
        except ValueError as e:
            print(f"Invalid data format: {e}")
            continue # turpinam ar nākamo rindu, ja dati nav pareizā formātā

        if time_s <= 0:
            print(f"Invalid time_s={time_s}. Must be > 0.")
            continue # turpinam ar nākamo rindu, ja time_s nav pozitīvs, jo dalīšana ar 0 vai negatīvu laiku nav jēdzīga

        speed = distance_m / time_s
        speeds.append(speed)

        print(f"Ātrums: {speed:.2f} m/s")

if speeds:
    avg_speed = sum(speeds) / len(speeds)
    print(f"Vidējais ātrums: {avg_speed:.2f} m/s")
else:
    print("Nav datu.")
