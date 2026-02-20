import json

data = {
    "title": "Programming",
    "year": 2026
}

json_string = json.dumps(data, indent=2)

print("JSON string:")
print(json_string)
