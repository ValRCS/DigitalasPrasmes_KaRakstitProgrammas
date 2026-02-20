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
# tā kā mums ir data vārdnīca, mēs varam izdrukāt katru atslēgu un tās vērtību, kā arī to datu tipu, lai redzētu, kā JSON datu tipi tiek konvertēti uz Python datu tipiem

for key, value in data.items():
    print(key, "→", type(value))
