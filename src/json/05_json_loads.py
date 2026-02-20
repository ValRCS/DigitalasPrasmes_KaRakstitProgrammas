import json

# izveidojam json formatētu string
# ievērojam trīs pēdiņas, lai varētu iekļaut vairākrindu tekstu, un JSON formātā tiek izmantoti dubultie pēdiņi ap atslēgām un vērtībām
json_text = """
{
    "name": "Anna",
    "age": 30,
    "active": true
}
"""

# mēs pārvērtīsm JSON tekstu atpakaļ Python objektā, izmantojot json.loads, kas konvertē JSON datus no teksta formāta uz Python datu struktūru
data = json.loads(json_text)

print(data)
print("Age:", data["age"])
