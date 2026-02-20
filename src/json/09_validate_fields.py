import json

# Assumes persona.json exists. Run 01_write_basic_json.py first.
with open("persona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

required_fields = ["name", "age"]

for field in required_fields:
    if field not in data:
        raise ValueError(f"Missing required field: {field}")

print("JSON structure valid.")
