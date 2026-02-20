import csv

# Assumes dati.csv exists. If not, run 01_write_basic_writer.py first.
with open("dati.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print(row)

# ierobežojums - ja CSV datnē ir galvene (header), tad tā tiks izdrukāta kā pirmā rinda, un tā nav datu rinda, bet tikai kolonnu nosaukumi. Ja vēlamies izlaist galveni, varam izmantot next(reader) pirms cikla, lai pārietu uz nākamo rindu.
