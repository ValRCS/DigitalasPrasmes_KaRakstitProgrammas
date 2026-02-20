import json

json_text = """
{
    "name": "Anna",
    "age": 30,
    "active": true
}
"""

data = json.loads(json_text)

print(data)
print("Age:", data["age"])
