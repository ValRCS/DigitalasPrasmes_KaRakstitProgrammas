import socket

# 1) Iegūstam datora vārdu (hostname)
hostname = socket.gethostname()

# 2) Mēģinām pārvērst hostname uz IP (bieži LAN IP vai 127.0.1.1 atkarībā no sistēmas)
ip = socket.gethostbyname(hostname)

print(f"Dators (hostname): {hostname}")
print(f"IP adrese (pēc hostname): {ip}")
