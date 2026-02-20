import json

# Assumes persona.json exists. Run 01_write_basic_json.py first.
with open("persona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print("Name:", data["name"])
print("Courses:", data["courses"])
