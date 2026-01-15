# 3x3 spēles laukums
laukums = [
["-", "-", "-"], # 0. rinda
["-", "-", "+"], # 1. rinda
["-", "-", "-"] # 2. rinda
]
print(laukums)

# es varu ciklot cauri un katru rindu drukāt atsevišķi
for rinda in laukums:
    print(rinda)

print("2 rinda ir")
# izdrukājam 2 rindu ar indeksu 1
print(laukums[1])

# savukārt 2 rindas 3 elements būs
print("Otras rindas trešais elements ir", laukums[1][2])

tabula = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Nolasīt vērtības
print(tabula[0][0]) # 1
print(tabula[1][2]) # 6
print(tabula[2][1]) # 8
# Nolasīt veselu rindu
print(tabula[0]) # [1, 2, 3]
print(tabula[1]) # [4, 5, 6]

# ieliksim laukumā 3 rinda pirmais elements X

# es varu mainīt kāda elementa saturu
laukums[2][0] = "X"

for rinda in laukums:
    print(rinda)

# var lietot if lai parbaudītu kādu sarakstu saraksta elementa saturu

if laukums[0][1] == "-":
    print("Brīvs var iet")
    laukums[0][1] = "X"
    print("Gajiens veikts")
else:
    print("Vieta aizņemta!")

for rinda in laukums:
    print(rinda)

if laukums[0][1] == "-":
    print("Brīvs var iet")
    laukums[0][1] = "X"
    print("Gajiens veikts")
else:
    print("Vieta aizņemta!")

for rinda in tabula:
    for elements in rinda:
        print(elements, end=" ")
    print() # tukša rinda

# ārējais cikls
for i in range(len(laukums)):
    # iekšējais cikls
    for j in range(len(laukums[i])):
        print(f"[{i}][{j}] = {laukums[i][j]}")

# Skaista tabulas izvade
print("  0 1 2") # Kolonnu numuri
for i in range(len(laukums)):
    print(i, end=" ") # Rindas numurs
    for j in range(len(laukums[i])):
        print(laukums[i][j], end=" ")
    print()

# mazā reizināšanas tabula no 0x0 līdz 5x5
# lai būtu vieglāk taisam tehniski 6x6 tabulu

ROWS = 5
COLS = 5
reiz_tab = []
for row in range(ROWS+1):
    print("Veidojam rindu", row)
    rinda = []
    reiz_tab.append(rinda)
    # taga reiz_tab[row] == rinda
    # iekšējais cikls
    for col in range(COLS+1):
        rinda.append(row*col)
        # alternatīva būtu
        # reiz_tab[row].append(row*col)
# izdrukājam tabulu
for rinda in reiz_tab:
    for elements in rinda:
        print(elements, end="\t")
    print()
