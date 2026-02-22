import socket # standarta bibliotēka tīkla savienojumiem

HOST = "127.0.0.1" # "localhost" nozīmē, ka serveris darbosies tikai uz šī datora
PORT = 5000 # izvēlamies portu, uz kura serveris klausīsies (0-65535, bet zem 1024 parasti ir rezervēti sistēmas procesiem)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT)) # šeit mēs sasaistām socket ar konkrētu adresi un portu
    # citi serveri nevarēs izmantot šo portu mūsu datorā, kamēr mūsu serveris ir aktīvs
    server.listen(1)
    print(f"TCP serveris klausās uz {HOST}:{PORT}")
    # te mēs zinam ka ir tikai viens klients, kas pieslēgsies, tāpēc listen(1) - tas nozīmē, ka serveris var apstrādāt vienu savienojumu vienlaikus
    conn, addr = server.accept()
    with conn:
        print("Pieslēdzās klients:", addr)
        data = conn.recv(1024)
        print("Saņēmu:", data.decode("utf-8", errors="replace")) # utf-8 jo tas ir visizplatītākais teksta kodējums, un errors="replace" nozīmē, ka, ja saņemtie dati nav derīgi utf-8, tie tiks aizstāti ar aizvietotāju simbolu

        # TCP gadījumā “atbilde” ir tipiska — klients saņem, ka serveris reaģē
        conn.sendall("ACK: saņēmu ziņu\n".encode("utf-8"))
