import json

data = {
    "title": "Programming",
    "year": 2026
}

# dumps ar s burtu s ir saīsinājums no "dump string", un tas tiek izmantots, lai konvertētu Python objektu (šajā gadījumā vārdnīcu) uz JSON formāta tekstu (string), nevis saglabāt to failā
json_string = json.dumps(data, indent=2)

print("JSON string:")
print(json_string)
# es varētu arī šeit šo json_string saglabāt failā, bet šoreiz mēs tikai izdrukājam to konsolē, lai redzētu, kā izskatās JSON formāts kā teksts
