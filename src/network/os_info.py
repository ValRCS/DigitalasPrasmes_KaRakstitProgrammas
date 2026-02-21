import platform

os_name = platform.system()   # "Windows", "Linux", "Darwin"
os_ver = platform.release()   # piem. "10", "11", "6.8.0-...", "22.04"

print(f"OS: {os_name} {os_ver}")
