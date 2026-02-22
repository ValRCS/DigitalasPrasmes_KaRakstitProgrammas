# apskatīsim socket bibliotēku, kas ļauj mums veidot tīkla savienojumus un sazināties ar citiem datoriem.
import socket # iebūvēta bibliotēka, kas nodrošina tīkla funkcionalitāti

# izveidosim socket objektu, kas būs mūsu savienojuma punkts
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET - IPv4, SOCK_STREAM - TCP savienojums

# uzstādām noildziu, lai socket negaidītu bezgalīgi
s.settimeout(1) # 1 sekundes

# pārbaudīsim portu 80 uz google.com, lai redzētu, vai tas ir atvērts
# izmantosim connect_ex, kas atgriež 0, ja savienojums ir veiksmīgs, un citu vērtību, ja nav veiksmīgs
# host = 'google.com'
host = 'rtu.lv'
port = 80
result = s.connect_ex((host, port))
if result == 0:
    print(f"Port {port} uz {host} ir atvērts.")
else:
    print(f"Port {port} uz {host} nav atvērts.")

# neaizmirstam aizvērt socket, kad esam pabeiguši
s.close()