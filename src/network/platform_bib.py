# apskatīsim platform bibliotēku, kas ļauj mums strādāt ar dažādām operētājsistēmām un platformām.
import platform # iebūveta bibliotēka, nav jāinstalē

# noskaidrosim, kāda operētājsistēma tiek izmantota
os_name = platform.system()
print(f"Operētājsistēma: {os_name}")

# versija
os_version = platform.version()
print(f"Operētājsistēmas versija: {os_version}")