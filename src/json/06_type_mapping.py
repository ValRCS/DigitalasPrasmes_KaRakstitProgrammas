import json

json_text = """
{
    "number": 10,
    "decimal": 2.5,
    "text": "hello",
    "flag": true,
    "nothing": null,
    "list": [1, 2, 3]
}
"""

data = json.loads(json_text)

for key, value in data.items():
    print(key, "→", type(value))
