# Tātad teksts jeb strings ir datu tips, kas satur rakstzīmju virkni.
# Teksta metodes ir iebūvētas funkcijas, kas ļauj manipulēt ar tekstu.
# Būtiski atcēriets ka pats oriģinālais teksts nemainās, 
# bet metodes atgriež jaunu tekstu ar veiktajām izmaiņām.

# Teksts tātad ir simbolu virkne, ko var apstrādāt ar dažādām metodēm.

# apskatīsim dažas tipiskas metodes upper(), lower() un capitalize()

mans_teksts = "Sveiki, Pasaule!"

viss_liels = mans_teksts.upper()  # Pārvērš visu tekstu lielajos burtos
visi_mazi = mans_teksts.lower()   # Pārvērš visu tekstu mazajos burtos

print("Oriģinālais teksts:", mans_teksts)
print("Teksts lielajos burtos:", viss_liels)
print("Teksts mazajos burtos:", visi_mazi)

# tātad ja es gribu savu tekstam tikai pirmo lielu tad izmanto capitalize()
pirmais_liels = mans_teksts.capitalize()  # Pārvērš pirmo burtu lielo, pārējos mazajos
print("Teksts ar pirmo lielo burtu:", pirmais_liels)

# es varu pārrakstīt oriģinālo mainīgo ja vēlos
mans_teksts = mans_teksts.upper()
print("Oriģinālais teksts pēc pārrakstīšanas:", mans_teksts)

# ja es gribēt atgūt originālu es varu izmanot title() metodi
mans_teksts = mans_teksts.title()  # Pārvērš katra vārda pirmo burtu lielo
print("Oriģinālais teksts pēc title() metodes:", mans_teksts)

# apskatīsm strip metodi
teksts_ar_tukšumiem = "   Sveiki, Pasaule!   "
# repr rāda tekstu ar visiem speciālajiem simboliem, piemēram, tukšumiem
print("Teksts ar tukšumiem:", repr(teksts_ar_tukšumiem))
teksts_bez_tukšumiem = teksts_ar_tukšumiem.strip()  # Noņem tukšumus no abām pusēm
print("Teksts bez tukšumiem:", repr(teksts_bez_tukšumiem))

# ir arī lstrip un rstrip metodes, kuras noņem tukšumus tikai no kreisās vai labās puses

# meklēsim kaut ko tekstā vispirms pārbaudism ar in operatoru
# esamības pārbaude
print("Vai tekstā ir 'saule'?", "saule" in mans_teksts)

# ar find vai index metodi varam atrast apakšvirknes pozīciju
pozicija = mans_teksts.find("Pasaule")  # Atgriež sākuma pozīciju vai -1, ja nav atrasts
print("Vārda 'Pasaule' pozīcija tekstā:", pozicija)

# mēs varam izdrukāt simbolu 8 pozīcijā
print("Simbols 8 pozīcijā:", mans_teksts[8]) # atceramies indekss sākas no 0

# skatamies visu no 8 pozīcijas līdz beigām
print("Teksts no 8 pozīcijas līdz beigām:", mans_teksts[8:])

# kā būtu ar visu pirms 8 pozīcijas
print("Teksts pirms 8 pozīcijas:", mans_teksts[:8]) # 8 šeit nav iekļauts
# 8 pozīcija ir 9tais simbols pēc kārtas

# pirmais simbols
print("Pirmais simbols:", mans_teksts[0])

#pēdējais simbols
print("Pēdējais simbols:", mans_teksts[-1])

# atradīsim saule pozīciju un izdrukāsim to
saule_pozicija = mans_teksts.find("saule")
print("Vārda 'saule' pozīcija tekstā:", saule_pozicija)
# un tagad recepte kā izdrukāt vārdu saule no teksta izmantojot to pozīciju
if saule_pozicija != -1:
    print("Vārds 'saule' tekstā:", mans_teksts[saule_pozicija:saule_pozicija + len("saule")])
# tam nav lielas jēgas ja nav mainīgais

# bet ja ir mainīgais tad ir jēga
adata = "iki"
pozicija_adata = mans_teksts.find(adata)
if pozicija_adata != -1:
    print(f"Vārds '{adata}' tekstā:", mans_teksts[pozicija_adata:pozicija_adata + len(adata)])
else:
    print(f"Vārds '{adata}' tekstā nav atrasts.")

# alternatīva find ir index metode
# tā atgriež pozīciju ja atrasts, bet ja nav atrasts tad izmet kļūdu

try:
    pozicija_index = mans_teksts.index("Pasaule")
    print("Vārda 'Pasaule' pozīcija ar index metodi:", pozicija_index)
except ValueError:
    print("Vārds 'Pasaule' nav atrasts ar index metodi.")

alfabets = "abcdefghijklmnopqrstuvwxyz"
# izdrukāsim katru otro burtu no alfabēta
print(alfabets[::2]) # tātad pēdejais ir solis

# kā būtu sākšanu no otrā simbola un katru trešo
print(alfabets[1::3])

# kā būtu apgriezt alfabētu
print(alfabets[::-1]) # atceramies solis ir negatīvs
# mēs to nesaglabājam mainīgajā, bet varam to izdarīt
apgriezts_alfabets = alfabets[::-1]
print("Apgriezts alfabēts:", apgriezts_alfabets)

# Python ir divi indeksi priekš simboliem un citiem virkņu tipiem
# viens ir pozitīvs kas sākas no 0 un iet uz priekšu
# otrs ir negatīvs kas sākas no -1 un iet atpakaļ

brokastis = "auzu putra ar avenēm"
print(brokastis)
# mēs varam izmantot replace metodi lai nomainītu daļu no teksta
jaunas_brokastis = brokastis.replace("avenēm", "banāniem")
print("Jaunas brokastis:", jaunas_brokastis)

# es varu nomainīt vienu simbolu piemēram u uz y
jaunas_brokastis2 = brokastis.replace("u", "y")
print("Jaunas brokastis ar y:", jaunas_brokastis2)

# mēs varam griezt uz izmanot + lai apvienot tekstus
vards = "Jānis"
uzvards = "Bērziņš"
pilns_vards = vards + " " + uzvards
print("Pilns vārds:", pilns_vards)
# mēs varam izmanot slice un griest atkal un apvienot
isvards = pilns_vards[:4] + pilns_vards[7:]
print("Īsāks vārds:", isvards)

# atceramies ka mums ir pilns Unicode atbalsts tekstam tas
# ietver arī emocijzīmes
emocijas = "Es mīlu Python! 🐍❤️"
print(emocijas)