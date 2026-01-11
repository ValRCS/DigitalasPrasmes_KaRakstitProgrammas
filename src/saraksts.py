# Tukšs saraksts
vardi = []

# ar gatavām dažām vērtībām
# pārrākstījām pāri vecajam tukšajam vardi sarakstam
vardi = ["Anna", "Jānis", "Valdis", "Līga"]

# saraksts ar skaitļiem
atzimes = [8,9,1,3,10,9]

# var arī jaukt, bet labāk glabāt līdzigas lietas
viskass = ["Atzīme", 9, "Pīrāgs", 3.1416926]

print("Pirmā", vardi[0])
print("Otrais", vardi[1])

print("Pēdējā", vardi[-1])
print("Arī Pēdējā", vardi[3])

# Izmantošana teikumā
print(f"Pirmais skolēns ir {vardi[0]}")
# Izvada: Pirmais skolēns ir Anna

# pievienojam Ilzi
vardi.append("Ilze") # modificē vardi ar jaunu ierakstu BEIGĀS

print(vardi)

# Pievienojam elementus
vardi.append("Anna")
vardi.append("Jānis")
print(vardi)

# Var pievienot arī mainīgo vērtību
# jauns_vards = input("Ievadi vārdu: ")
# vardi.append(jauns_vards)
# print(vardi)

# nomainam otro elementu - INDEKSS 1 !!!
vardi[1] = "Mārtiņš"
print(vardi)

temperaturas = [-3.2, -2.8, 99.0, 0.0, 1.3]
# 99.0 ir kļūda, labojam trešo elementu
temperaturas[2] = -1.5
print(temperaturas)
# Izvada: [-3.2, -2.8, -1.5, 0.0, 1.3]

# Pārrēķins
atzimes = [5, 8, 6]
print(atzimes)
atzimes[0] = atzimes[0] + 4 # Palielinām pirmo elementu par 4
print(atzimes) # [9, 8, 6]

# garumi
print(len(vardi))
print(len(atzimes))

# Vidējā vērtība
atzimes = [8, 9, 7, 10]
videja = sum(atzimes) / len(atzimes)
print(f"Vidējā atzīme: {videja}")
# Izvada: Vidējā atzīme: 8.5
# Pēdējais elements
print(vardi[len(vardi) - 1]) # nevajag lietot jo mums ir NEGATĪVIE INDEKSI!
print(vardi[-1]) # TAS pats bet īsāk!

# Ja mums ir vienāda datu tipa dati sarakstā tad var veikt papildu operācijas
# skaitliskiem datu tipem var veikt sum,min,max un str tipiem var veikt min/max

temperaturas = [-3.2, -2.8, -1.5, 0.0, 1.3, 2.1, 5] #var jaukt int un float
# Statistika
print(f"Summa: {sum(temperaturas)}")
print(f"Vidējā: {sum(temperaturas) / len(temperaturas)}")
print(f"Maksimālā: {max(temperaturas)}")
print(f"Minimālā: {min(temperaturas)}")