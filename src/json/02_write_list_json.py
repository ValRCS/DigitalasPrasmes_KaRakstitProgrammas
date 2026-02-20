import json

# mums ir Python saraksts (list) ar vārdnīcām (dictionaries), kur katra vārdnīca satur informāciju par studentu
students = [
    {"name": "Anna", "age": 30},
    {"name": "Pēteris", "age": 28},
    {"name": "Jānis", "age": 25}
]

with open("studenti.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)

# json tas būs masīvs saraksts ar 3 objektiem, kur katrs objekts ir vārdnīca ar "name" un "age" atslēgām
print("Saved studenti.json")
