vardi = ["Anna", "Jānis", "Ilze", "Mārtiņš", "Līga"]

# ar for ciklu - īsi un efektīgi
for vards in vardi:
    print(vards) # izdrukājam katru elementu atsevišķi

atzimes = [8, 9, 7, 10, 6]
for atzime in atzimes:
    print(f"Atzīme: {atzime}")

# cikla beigās atzime būs pēdejā vertība
print(f"Beigās atzīme joprojam ir {atzime}")

vards = "Python"
for burts in vards:
    print(burts)

skaitli = [1, 2, 3, 4, 5]
summa = 0
for skaitlis in skaitli:
    summa = summa + skaitlis
print(f"Summa: {summa}")
# ja atceramies šeit varējām arī izmantot sum
print(f"Aŗi {sum(skaitli)}")
# bet sarežģītākām darbībām cikls būs īstais risinājums

# izvadam no 0 līdz 4
for i in range(5):
    print(i)

# Izvadīt skaitļus no 1 līdz 10
for i in range(1, 11):
    print(i)

# Pāra skaitļi no 0 līdz 10
for i in range(0, 11, 2):
    print(i) # 0, 2, 4, 6, 8, 10

# Saraksta indeksi
vardi = ["Anna", "Jānis", "Ilze"]
# klasisks programēšanas paņēmiens
for i in range(len(vardi)):
    print(f"{i}: {vardi[i]}")

# Python stils uzskata šo par piemērotāku, iegūstam uzreiz divus mainīgos katram elementam
# pirmais index otrais pats elements
for index, item in enumerate(vardi):
    print(f"{index}: {item}")

# skaitam
n = 1
while n <= 5:
    print(n)
    # ar roku tagad jāpalielina n
    n = n + 1 # kritiski, varēja arī n += 1 īsāks pieraksts

# cik būs n beigās?
print(f"Beigās n ir {n}")

# Lietotāja ievade līdz pareizai atbildei
atbilde = "" # tukšs teksts sākkuma
skaititajs = 0
# while atbilde != "jā":
#     atbilde = input("Vai vēlies beigt? (jā/nē): ")
#     skaititajs += 1 # pieliekam 1 pie skaititaja
#     print(f"Kaut ko daram jau {skaititajs} reizi")

# break mums ļauj iziet ārā no cikla gan for gan while

for i in range(10):
    if i == 5:
        print("Pietiek", i)
        break # turpinam ārpus cikla
    print(i)

print("arpus cikla")

for i in range(8):
    if i == 2:
        print("Izlaižām", i)
        continue # lec atpakaļ uz cikla sākumu un tad būs jauna vērtība
    print(i)
print("Cikls beidzies")

while True: # mūžīgais cikls bet  iekšā ar break
    atbilde = input("Vai vēlies beigt? (jā/nē): ")
    if atbilde.lower() == "jā":
        print("Beidzam ciklu")
        break
    else:
        print("Turpinām ciklu")

print("Cikls atkal beidzies")