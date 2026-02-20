import json

# Assumes persona.json exists. Run 01_write_basic_json.py first.
with open("persona.json", "r", encoding="utf-8") as f:
    # mēs pārvērtīsm JSON tekstu atpakaļ Python objektā, izmantojot json.load, kas lasa no faila un konvertē JSON datus uz Python datu struktūru
    data = json.load(f) # šeit data būs Python datu struktūra, kas atbilst JSON datiem, kas tika saglabāti persona.json failā. Šajā gadījumā tas būs vārdnīca (dictionary) ar atslēgām "name", "age", "is_student" un "courses".

# print data strādās vienmēr, jo data ir Python objekts (šajā gadījumā vārdnīca), un mēs varam piekļūt tā saturam, izmantojot atslēgas, piemēram, data["name"] vai data["courses"], lai iegūtu konkrētas vērtības no vārdnīcas.
print(data)
# savukārt šeit iespējams, ka mēs vēlamies izdrukāt tikai konkrētas daļas no data, piemēram, vārdu un kursus, 
# lai redzētu, kā piekļūt šīm vērtībām no vārdnīcas, kas tika ielādēta no JSON faila.
# te mums ir jāzin ka name un courses tiešām eksistē data vārdnīcā, pretējā gadījumā mēs saņemtu KeyError, ja mēģinātu piekļūt neeksistējošai atslēgai.
try:
    print("Name:", data["name"]) # te būs string "Jānis", jo tā ir vērtība, kas atbilst atslēgai "name" data vārdnīcā
    print("Courses:", data["courses"]) # šeit būs saraksts ["Python", "AI", "Algorithms"], jo tā ir vērtība, kas atbilst atslēgai "courses" data vārdnīcā
    # pieliksim neekstra atslēgu, lai parādītu, kas notiek, ja mēģinām piekļūt atslēgai, kas nav data vārdnīcā
    print("Nonexistent key:", data["nonexistent_key"])
except KeyError as e:
    print(f"Key {e} not found in data.")

