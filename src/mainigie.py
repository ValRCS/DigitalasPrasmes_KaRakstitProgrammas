# bez mainīga - fiksēts skaitlis
print("Skaitlis ir 10")

# Ar mainīgo - elastīgi
skaitlis = 25  # šeit mēs uzstādam mainīgo skaitlis, kas norāda uz vērtību 25
print(f"Skaitlis ir {skaitlis}")
print(f"Skaitlis joprojām ir {skaitlis}")
print(skaitlis)

# Var mainīt vērtību
skaitlis = 42 # šeit mēs pārrakstam norādi un skaitlis norāda uz 42
print(f"Skaitlis tagad ir {skaitlis}")
print(f"Skaitlis turpina būt  {skaitlis}")
print("Daram ko vel")
print(f"Skaitlis joprojām ir {skaitlis}")

katete1: float = 3.0
skaits: int = 20
# Piezīme : float un : int praksē izmanto ļoti reti
print(katete1)
print(skaits)
# Python ir dinamiska valoda, datu tipi tiek pielāgoti automātiski mainīgiem

# mēs varam veikt daudzas matemātiskas funkcijas ar math biblioteku
# tā nāk līdz Python bet jāaktivizē
import math # vienā programmā vajag importēt tikai vienreiz vienu biblioteku

katete2 = 4.0 # automātiski būs float tips jo .0 to norāda
hipotenuza = math.sqrt(katete1**2 + katete2**2)

print("Hipotenūza būs", hipotenuza)

# šie visi būs float
a = 2.0
b = 5.0
c = 3.0
D = b**2 - 4*a*c
sakne_D = math.sqrt(D)

print("===============================")
print("Diskriminants D:\t", D)
print("Kvadrātsakne no D:\t", round(sakne_D, 2))
print("===============================")

