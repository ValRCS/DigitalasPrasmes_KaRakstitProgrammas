import socket

def resolve(hostname: str):
    infos = socket.getaddrinfo(hostname, None)  # atgriež sarakstu ar iespējamām adresēm
    ips = sorted({item[4][0] for item in infos})
    return ips

if __name__ == "__main__":
    host = "google.com"
    ips = resolve(host)
    print(f"{host} IP adreses:")
    for ip in ips:
        print(" -", ip)
