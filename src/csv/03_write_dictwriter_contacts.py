import csv

contacts = [
    {"name": "Jānis", "email": "janis@example.com"},
    {"name": "Anna", "email": "anna@site.lv"},
]

fieldnames = ["name", "email"]

with open("kontakti.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(contacts)

print("Saved kontakti.csv")
