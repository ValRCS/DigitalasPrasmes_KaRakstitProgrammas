# networking_examples

Šajā mapē ir vienkārši Python piemēri par tīklu pamatiem (balstīti uz prezentācijas tematiem):
- Datora nosaukums un IP (`hostname_ip.py`)
- OS noteikšana (`os_info.py`)
- Savienojamības pārbaude ar `ping` (`ping_check.py`)
- DNS nosaukums → IP (`dns_lookup.py`)
- TCP serveris/klients (`tcp_server.py`, `tcp_client.py`)
- UDP serveris/klients (`udp_server.py`, `udp_client.py`)

## Prasības
- Python **3.10+** (der arī 3.8+, bet ieteicams 3.10/3.11/3.12)
- Nekādu ārējo bibliotēku nav nepieciešams (tikai standarta bibliotēka)

## Kā palaist (Windows 10/11)

Atver **PowerShell** mapē `networking_examples`.

Pārbaudi Python:
```powershell
python --version
```

### 1) Hostname un IP
```powershell
python .\hostname_ip.py
```

### 2) OS informācija
```powershell
python .\os_info.py
```

### 3) Ping tests
```powershell
python .\ping_check.py
```

### 4) DNS lookup
```powershell
python .\dns_lookup.py
```

### 5) TCP demo
**1. logs (serveris):**
```powershell
python .\tcp_server.py
```

**2. logs (klients):**
```powershell
python .\tcp_client.py
```

### 6) UDP demo
**1. logs (serveris):**
```powershell
python .\udp_server.py
```

**2. logs (klients):**
```powershell
python .\udp_client.py
```

## Kā palaist (Ubuntu / Linux)

Atver termināli mapē `networking_examples`.

Pārbaudi Python:
```bash
python3 --version
```

### 1) Hostname un IP
```bash
python3 ./hostname_ip.py
```

### 2) OS informācija
```bash
python3 ./os_info.py
```

### 3) Ping tests
```bash
python3 ./ping_check.py
```

### 4) DNS lookup
```bash
python3 ./dns_lookup.py
```

### 5) TCP demo
**1. terminālis (serveris):**
```bash
python3 ./tcp_server.py
```

**2. terminālis (klients):**
```bash
python3 ./tcp_client.py
```

### 6) UDP demo
**1. terminālis (serveris):**
```bash
python3 ./udp_server.py
```

**2. terminālis (klients):**
```bash
python3 ./udp_client.py
```

## Tipiskas problēmas

### “Ping” neiet cauri
- Iespējams, interneta nav, DNS nedarbojas, vai ICMP ir bloķēts tīklā.
- Izmēģini citu hostu (piem., `1.1.1.1` vai `8.8.8.8`).

### TCP/UDP serveris nepalaižas (ports aizņemts)
- Nomaini portu failā (piem., 5000 → 5001; 6000 → 6001).

### Windows ugunsmūris
- Pirmajā reizē Windows var pajautāt atļauju Python piekļuvei tīklam — atļauj lokālajā tīklā (Private networks), ja izmanto `127.0.0.1` demo.
