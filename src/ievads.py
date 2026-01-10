# vards = input("Kā Tevi sauc?")
# print(f"Sveiciens, {vards}")
# # varam turpinam rīkots ar vards saturu līdz programmas beigām
# print(type(vards)) # so tips būs str

# # Ievade un pārveidošana
# vecums_str = input("Cik Tev gadu? ")
# # notiek pārveidošana
# vecums =  int(vecums_str)

# # Var darīt uzreiz
# garums = float(input("Ievadi garumu (m): "))

# # varam reķināt tagad
# gadi_pec_10 = vecums + 10
# print(f"Pēc 10 gadiem Tev būs {gadi_pec_10} gadi")

# izstiepies = garums + 0.25 # jo metri tika vadīti
# print(f"{vards}, ja kārtīgi izaugsi par 25cm tad no {garums} m būsi {izstiepies} m garš")

# # Aprēķināsim taisnstūra laukumu
# print("Taisnstūra laukuma aprēķināšana")
# garums = float(input("Ievadi garumu (cm): "))
# platums = float(input("Ievadi platumu (cm): "))
# laukums = garums * platums
# print(f"Taisnstūra laukums: {laukums} cm²")

# varam lietot try / except bloku lai ķertu  kļūdas apstrādē un ne tikai
try:
    vecums = int(input("Cik tev gadu? "))
    print(f"Tev ir {vecums} gadi")
    print("Tev ir {vecums} gadi") # bez f būs vienkārši teksts
except ValueError: # laba prakse ir ķert konkrētas kļūdas
    print("Kļūda! Lūdzu, ievadi skaitli!")
# Ja ievada "16" → Tev ir 16 gadi
# Ja ievada "sešpadsmit" → Kļūda! Lūdzu, ievadi skaitli!

# Formatēšana ar decimāldaļām
cena = 12.5
print(f"Cena: {cena:.2f} EUR") # 12.50 EUR
# Aprēķini iekš f-string
a = 5
b = 3
print(f"Summa: {a + b}") # Summa: 8

print("Programmas beigas") # vienmēr izpildas