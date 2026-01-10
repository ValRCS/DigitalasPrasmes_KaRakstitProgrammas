print(5+3)
print(10-4)
print(6*2)
print(15/3) # žeit iegustam float datu tipu
print(17//5) # jo bez atilkuma iegūstam veselu skaitli (int)
print(17%5) # atlikums 2
print(2**3) # kubā 3 pakape

# jāatceras ka mēs neko nesaglabājām no šim darbībām
# ja gribam saglabāt tad vajag glabāt rezultātu mainīgos
rezultats = 5 + 3
print(rezultats)

# tagad salīdzināšana 
# iegūsim True vai False (Boolean datu tips)
print(5 == 5) # True
print(5 != 3) # arī True
print(10>5) # arī True
print(3<7) # arī patiesam
print(5>=5) # arī True
print(4 <= 6) # arī True

print(10 == 20) # False
print(2*2 == 4) # True
print(2*2 == 5) # False

print("Pārbaudīsim vecumu!")

# vecums = 18 # pieškiram vērtību mainīgajam
vecums = 16 # pieškiram vērtību mainīgajam

if vecums >= 18:
    print("Esi pilngadīgs")
    print("Vari Balsot!")
else: # izpildās pie ja False ir if pārbaude
    print("Tu esi nepilngadīgs")
    print("Varbūt vēl drusku pagaidi")
    # varam turpināt šeit ar instrukcijām gadijumam, ja ir False  vecums >= 18

# esam ārā no if else bloka 
print("Programma turpinās jebkādā gadījumā")

# Ja nosacījums ir True, izpilda ar atkāpi izlīdzināto pirmkodu
# Ja nosacījums ir False, ar atkāpi izlīdzināto pirmkodu izlaiž

# atzime = 8
# atzime = 3
atzime = 10

if atzime >= 9:
    print("Teicami!")
elif atzime >= 7:
    print("Labi!")
elif atzime >= 5:
    print("Viduvēji.")
else:
    print("Jāuzlabo.")
# Pārbauda nosacījumus pēc kārtas
# Izpilda PIRMO True bloku

# and piemērs
vecums = 20
ir_students = True
# and būs True ja tikai ABI ir True
if vecums >= 18 and ir_students:
    print("Saņem studentu atlaidi.")
else:
    print("Jābūt gan 18+ gan studentam!")
# or piemērs jābūt True vismaz vienam
diena = "sestdiena"
if diena == "sestdiena" or diena == "svētdiena":
    print("Brīvdiena!")
# not piemērs
# taisot mainīgos kur turēsim False and True Boolean vērtības
# laba prakse ir sākt tos ar ir vai is vai are
# is_raining, ir_lietus
ir_lietus = False
if not ir_lietus:
    print("Var iet pastaigāties.")

# Biļešu cenu aprēķins
vecums = int(input("Ievadi savu vecumu: "))
ir_students = input("Vai esi students? (jā/nē): ")
if vecums < 7:
    cena = 0
    print("Bezmaksas!")
elif vecums < 18:
    cena = 3
    print(f"Bērnu biļete: {cena} EUR")
elif ir_students == "jā":
    cena = 5
    print(f"Studentu biļete: {cena} EUR")
else:
    cena = 8
    print(f"Pieaugušā biļete: {cena} EUR")

# Esam atpakaļ globaļa blokā
print("Viss beidzies laimīgi")