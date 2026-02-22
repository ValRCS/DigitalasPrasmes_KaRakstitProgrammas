import socket

HOST = "127.0.0.1" # ip adrese kurā darbojas serveris, "localhost" nozīmē, ka tas darbosies tikai uz šī datora
PORT = 5000 # ports, uz kura serveris klausās (0-65535, bet zem 1024 parasti ir rezervēti sistēmas procesiem)

# mums jāzina ka serveris ir jau palaists, pirms mēs mēģinām pievienoties kā klients
# atceramies
# AF_INET - IPv4, SOCK_STREAM - TCP savienojums
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("Sveiki! Šis ir TCP ziņojums.".encode("utf-8"))

    reply = client.recv(1024)
    print("Servera atbilde:", reply.decode("utf-8", errors="replace"))
    # atkal lietojam utf-8 kodējumu un errors="replace", lai izvairītos no problēmām, ja serveris nosūta datus, kas nav derīgi utf-8 formātā
