import socket

HOST = "127.0.0.1"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto("Sveiki! Šis ir UDP ziņojums.".encode("utf-8"), (HOST, PORT))

    # Ja serveris atbild, varam saņemt; ja neatbild, šis var “karāties” (tāpēc timeout)
    client.settimeout(2.0)
    try:
        data, addr = client.recvfrom(2048)
        print("Servera atbilde:", data.decode("utf-8", errors="replace"), "no", addr)
    except TimeoutError:
        print("Serveris neatbildēja laikā (UDP gadījumā tas ir normāli).")
