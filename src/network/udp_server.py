import socket

HOST = "127.0.0.1"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"UDP serveris klausās uz {HOST}:{PORT}")

    data, addr = server.recvfrom(2048)
    print("Saņēmu no", addr, ":", data.decode("utf-8", errors="replace"))

    # UDP gadījumā atbilde nav obligāta, bet var sūtīt
    server.sendto("UDP: saņēmu".encode("utf-8"), addr)
