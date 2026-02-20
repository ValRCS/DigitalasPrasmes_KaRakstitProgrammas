import json

students = [
    {"name": "Anna", "age": 30},
    {"name": "Pēteris", "age": 28},
    {"name": "Jānis", "age": 25}
]

with open("studenti.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)

print("Saved studenti.json")
