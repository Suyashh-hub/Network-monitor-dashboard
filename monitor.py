import os

def ping_host(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    return "UP" if response == 0 else "DOWN"
