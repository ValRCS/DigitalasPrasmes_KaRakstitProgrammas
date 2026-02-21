import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall("Sveiki! Šis ir TCP ziņojums.".encode("utf-8"))

    reply = client.recv(1024)
    print("Servera atbilde:", reply.decode("utf-8", errors="replace"))
