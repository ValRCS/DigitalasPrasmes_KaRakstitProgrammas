import json

bad_json = "{ name: Jānis }"  # invalid JSON (keys must be quoted)

# ja sagaidāms ka iespējamas kļūdas
# tad izmantojam try except bloku
try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print("JSON parsing error:")
    print(e)
