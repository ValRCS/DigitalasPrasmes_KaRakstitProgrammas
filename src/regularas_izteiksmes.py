# runāsim par regulārajām izteiksmēm
import re
# kapēc vispar vajadzētu regulārās izteiksmes?
# piemerām
text = "Mans telefons    ir 29123456,un prezidents@example.com valdis.saulespurens@rtu.lv"
# mēs nevaram izmantot text.isdigit() jo tekstā ir arī burti, bet mēs gribam pārbaudīt vai tekstā ir telefona numurs
# garums arī mums īsti neder

# re.search() - meklē tekstā atbilstošu paraugu un atgriež pirmo atrasto atbilstību
match = re.search(r'\d{8}', text)
if match:
    print("Telefona numurs atrasts:", match.group())

# re.findall() - meklē tekstā visus atbilstošos paraugus un 
# atgriež sarakstu ar visām atrastajām atbilstībām
# atradīsim visus e-pasta adreses tekstā
emails = re.findall(r'\w+@\w+\.\w+', text)
print("E-pasta adreses:", emails)

# tad re.fullmatch() - pārbauda vai viss teksts atbilst paraugam
# parbaudīsim kuponu
kods = "DZINTARI2024"
if re.fullmatch(r'[A-Z0-9]{6,12}', kods):
    print("Kods ir derīgs")
else:
    print("Kods nav derīgs")

# tad mums ir re.sub() - aizstāj tekstā atbilstošus paraugus ar citu tekstu
# aizstāsim telefona numuru ar zvaigznītēm
text_with_stars = re.sub(r'\b\d{8}\b', '********', text)
print("Teksts ar zvaigznītēm:", text_with_stars)

# tad visbeidzot re.split() - sadala tekstu pēc atbilstošiem paraugiem
# sadalīsim tekstu pēc atstarpēm un komatiem
parts = re.split(r'[ ,]+', text)
print("Teksta daļas:", parts)

# Kur skatītites tālāk? 
# https://docs.python.org/3/library/re.html
# Grāmatas par regulārajām izteiksmēm:
# "Mastering Regular Expressions" by Jeffrey E.F. Friedl
# "Regular Expressions Cookbook" by Jan Goyvaerts and Steven Levithan

# Tīmekļa lapas testēšanai:
# https://regex101.com/
