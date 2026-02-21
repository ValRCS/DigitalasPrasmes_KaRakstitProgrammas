import platform
import subprocess

def ping(host: str, count: int = 4) -> bool:
    os_name = platform.system()

    # Windows: ping -n 4
    # Linux/macOS: ping -c 4
    param = "-n" if os_name == "Windows" else "-c"

    cmd = ["ping", param, str(count), host]
    print("Komanda:", " ".join(cmd))

    # capture_output=True lai savāktu tekstu; text=True lai būtu str
    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)

    return result.returncode == 0

if __name__ == "__main__":
    ok = ping("google.com", count=2)
    print("PING rezultāts:", "OK" if ok else "NEIZDEVĀS")
