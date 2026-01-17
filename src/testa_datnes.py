# šodien apskatīsim teksta datnes jeb failus

# mums ir datne tautasdziesma.txt kuru vēlamies atvērt un izlasīt tās saturu
# atveram datni lasīšanas režīmā

datne = open("tautasdziesma.txt", mode="r", encoding="utf-8")
# datne ir straume uz datni
saturs = datne.read()
# aizveram datni
datne.close() # kritiski ir aizvērt datni pēc lasīšanas vai rakstīšanas

# mums ir pieeja datnes saturam mainīgajā saturs
print(saturs)
# saturs ir stringa tipa mainīgais
print(type(saturs))

# mēs varētu nolasīt arī rindiņas visas uzreiz
datne = open("tautasdziesma.txt", mode="r", encoding="utf-8")
rindas = datne.readlines()
datne.close() # atkal uzreiz aizveram datni

print(rindas)
print(type(rindas)) # rindas ir saraksta tipa mainīgais

# lielos failus es varētu nelasīt uzreiz, bet pa rindiņām
datne = open("tautasdziesma.txt", mode="r", encoding="utf-8")
# šādi var apstrādāt arī pat 1TB lielu teksta datni
for rinda in datne:
    # drukāsim tikai rindas kuras sākas ar P vai p
    if rinda.startswith("P") or rinda.startswith("p"):
        print(rinda.upper(), end="") # izdrukājam rindu bez liekajiem atstarpēm un jaunās rindas simboliem
# Cikls beidzas, bet datne vēl nav aizvērta
datne.close()
print() # izdrukājam tukšu rindu
print("Datne aizvērta.")

# atveram faila straumi rakstīšanas režīmā, vecais fails tiks pārrakstīts
f = open("sveiki.txt", mode="w", encoding="utf-8")
f.write("Sveiki!\n")
f.write("Šo tekstu failā ierakstīja programma!")
f.close()

# atvērsiim faila straumi papildināšanas režīmā, vecais fails netiks pārrakstīts
f = open("sveiki.txt", mode="a", encoding="utf-8")
f.write("\nŠo tekstu failā ierakstīja programma papildināšanas režīmā!")
f.close()

# izmantosim with konteksta pārvaldnieku lai automātiski aizvērtu datni
with open("tautasdziesma.txt", mode="r", encoding="utf-8") as datne:
    saturs = datne.read()
    print("Datnes saturs ar with konteksta pārvaldnieku:")

    # datne vēl ir atvērta šeit
# šeit datne jau ir automātiski aizvērta
print("Datne ar with konteksta pārvaldnieku ir aizvērta.")
print(saturs)

# izmantosim konteksta pārvaldnieku lai ierakstītu datni kurā ir rindas ar vārdu pieci

with open("tautasdziesma.txt", mode="r", encoding="utf-8") as lasama_datne:
    with open("tautasdziesma_pieci.txt", mode="w", encoding="utf-8") as rakstama_datne:
        for rinda in lasama_datne: # strādās arī ar ļoti lielām datnēm
            # šeit varat paši izdomāt savu loģiku
            if "pieci" in rinda.lower(): # atrādis arī ar Pieci, pādomājiem kāpēc?
                rakstama_datne.write(rinda)
    # šeit ir aizvērta rakstāma_datne bet lasama_datne vēl ir atvērta

# šeit abas datnes ir jau aizvērtas automātiski