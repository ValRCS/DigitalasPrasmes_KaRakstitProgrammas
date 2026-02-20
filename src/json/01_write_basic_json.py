import json

data = {
    "name": "Jānis",
    "age": 25,
    "is_student": True,
    "courses": ["Python", "AI", "Algorithms"]
}

with open("persona.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Saved persona.json")
