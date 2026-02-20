import json

# nolasam datus
with open("persona.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# modificējam datus Python objektā (vārdnīcā), piemēram, palielinām vecumu par 1 un pievienojam jaunu kursu sarakstam
data["age"] += 1
data["courses"].append("Data Science")

# varējam arī rakstīt virsū vecajam failam persona.json, bet šoreiz izveidosim jaunu failu persona_updated.json, lai saglabātu gan veco, gan jauno versiju
with open("persona_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Updated JSON saved.")
