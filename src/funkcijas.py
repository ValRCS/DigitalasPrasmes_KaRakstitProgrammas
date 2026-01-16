# Tātad funkcijas - atkārtoti izmantojami koda bloki, kas veic konkrētu uzdevumu.

def sveiciens():
    # sākaas funkcijas sveiciens koda bloks
    print("Sveiciens! Šī ir mana pirmā funkcija.")

# mēs vēl neesam izsaukuši funkciju, tāpēc nekas netiks izvadīts
sveiciens()  # šeit mēs izsaucam funkciju, un tiks izvadīts sveiciens
sveiciens()  # šeit mēs izsaucam funkciju, un tiks izvadīts sveiciens

# funkcijas ar parametriem
def sveiciens_vards(vards):
    print(f"Sveiciens, {vards}!")
    # vēl varam pievienot vairāk funkcionalitātes šeit
    print(f"Prieks tevi redzēt, {vards}!")

sveiciens_vards("Anna")  # izsaucam funkciju ar parametru "Anna"
sveiciens_vards("Jānis")  # izsaucam funkciju ar parametru "Jānis"

mans_vards = "Valdis"
sveiciens_vards(mans_vards)  # izsaucam funkciju ar mainīgo kā parametru

def kvadrats(skaitlis):
    return skaitlis * skaitlis  # atgriež skaitļa kvadrātu

print(kvadrats(5))  # izsaucam funkciju un izvadām rezultātu
# mēs varam saglabāt rezultātu mainīgajā
rezultats = kvadrats(10)
print(f"10 kvadrātā ir {rezultats}")

# salīdziniet ar funkciju bez atgriešanas vērtības
def izdrukat_kvadratu(skaitlis):
    # šāda funkcija nav elastīga, jo tā tikai izdrukā rezultātu fiksētā veidā
    print(skaitlis * skaitlis)
    # ja nav return tad automatiski tiek atgriests None

izdrukat_kvadratu(7)  # izsaucam funkciju, kas izdrukā kvadrātu
# ja mēģinām saglabāt rezultātu, tas būs None
rezultats2 = izdrukat_kvadratu(8)
print(f"Rezultāts ir {rezultats2}")  # izdrukās "Rezultāts ir None"

# mēs varam padot vairākus parametrus
def aprekinat_laukumu(garums, platums):
    return garums * platums  # atgriež laukumu

laukums1 = aprekinat_laukumu(5, 10)
print(f"Laukums ir {laukums1}")  # izvada laukumu

# sarežģitākās funkcijās mēs varam veidot mainīgos iekš funkcijas
def apraksts_vards_uzvards(vards, uzvards):
    pilns_vards = f"{vards} {uzvards}"
    # te vēl varētu ko darīt ar pilno vārdu
    return pilns_vards

pilns = apraksts_vards_uzvards("Inese", "Bērziņa")
print(f"Pilns vārds ir {pilns}")

# kā būtu are trijstura malām?
def trijstura_perimetrs(mala1, mala2, mala3):
    return mala1 + mala2 + mala3

perimetrs = trijstura_perimetrs(3, 4, 5)
print(f"Trijstūra perimetrs ir {perimetrs}")

# mēs varam veidot funkcijas kas izsauc vēl funkcijas

# piemēram ēšanas funkcija
def ediens(veids):
    print(f"Es ēdu {veids}.")

# tagad funkcija, kas saņem sarakstu ar ēdieniem un izsauc ēšanas funkciju katram
def edinasana(edienu_saraksts):
    for ediena_veids in edienu_saraksts:
        ediens(ediena_veids)

mana_maltite = ["ābols", "maize", "siers"]  # saraksts ar ēdieniem
edinasana(mana_maltite)  # izsaucam ēdināšanas funkciju ar sarakstu

print("Programmas beigas")  # programmas beigas