# apskatīsim socket bibliotēku, kas ļauj mums veidot tīkla savienojumus un sazināties ar citiem datoriem tīklā.
import socket # iebūveta bibliotēka, nav jāinstalē

# iegūstam datora vārdu
hostname = socket.gethostname()
print(f"Datora vārds: {hostname}")

# iegūstam datora IP adresi
ip_address = socket.gethostbyname(hostname)
print(f"Datora IP adrese: {ip_address}")