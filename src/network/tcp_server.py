import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"TCP serveris klausās uz {HOST}:{PORT}")

    conn, addr = server.accept()
    with conn:
        print("Pieslēdzās klients:", addr)
        data = conn.recv(1024)
        print("Saņēmu:", data.decode("utf-8", errors="replace"))

        # TCP gadījumā “atbilde” ir tipiska — klients saņem, ka serveris reaģē
        conn.sendall("ACK: saņēmu ziņu\n".encode("utf-8"))
