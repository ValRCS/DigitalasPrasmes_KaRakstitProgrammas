import json

# Assumes studenti.json exists. Run 02_write_list_json.py first.
with open("studenti.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(json.dumps(data, indent=4, ensure_ascii=False))
