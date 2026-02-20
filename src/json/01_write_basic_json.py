import json # atkal izmantojam iebūvēto Python json moduli, lai strādātu ar JSON datiem

# izveidojam Python vārdnīcu (dictionary), kas satur dažādus datu tipus, lai parādītu, kā tie tiek saglabāti JSON formātā
data = {
    "name": "Jānis",
    "age": 25,
    "is_student": True,
    "courses": ["Python", "AI", "Algorithms"]
}

# atveram teksta failu "persona.json" rakstīšanas režīmā ("w") un norādām kodējumu "utf-8", lai nodrošinātu pareizu rakstzīmju apstrādi
with open("persona.json", "w", encoding="utf-8") as f:
    # dump sagaida ka f būs atvērts faila objekts, kurā tiks saglabāts JSON dati, un data ir Python objekts, ko mēs vēlamies saglabāt JSON formātā
    json.dump(data, f, indent=4, ensure_ascii=False)
    # ievērojam ensure_ascii=False, lai saglabātu latviešu rakstzīmes un 
    # indent=4, lai padarītu JSON failu vieglāk lasāmu

print("Saved persona.json")
