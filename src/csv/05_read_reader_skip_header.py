import csv

# Assumes dati.csv exists. If not, run 01_write_basic_writer.py first.
with open("dati.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    headers = next(reader)  # skip header row lasam atsevišķi, lai varētu to izdrukāt vai izmantot kā lauku nosaukumus
    print("Headers:", headers)

    for row in reader:
        name = row[0]
        age_text = row[1] # mums nāk iekšā teksts, bet mēs zinām, ka tas ir skaitlis, tāpēc veiksim tipu konversiju
        age = int(age_text)  # type conversion, te var arī būt try-except bloks, ja nav pārliecības, ka dati ir korekti
        print(f"{name} is {age} years old")
