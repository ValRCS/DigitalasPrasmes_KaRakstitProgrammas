import json

# Assumes persona.json exists. Run 01_write_basic_json.py first.
with open("persona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# varam uzstādīt kādi lauki ir obligāti, lai mūsu JSON dati būtu derīgi, piemēram, mēs varam pieprasīt, lai katram ierakstam būtu "name" un "age" lauki
required_fields = ["name", "age"]
# pamēģiniet pielikt kādu citu lauku, piemēram, "email", un redzēt, kas notiek, ja tas nav data vārdnīcā

for field in required_fields:
    if field not in data:
        raise ValueError(f"Missing required field: {field}")

print("JSON structure valid.")
