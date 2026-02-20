import json

with open("persona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["age"] += 1
data["courses"].append("Data Science")

with open("persona_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Updated JSON saved.")
