import os
import subprocess
import socket

def detect_proxy():
    proxy_vars = ["HTTP_PROXY", "HTTPS_PROXY"]
    proxies = {p: os.environ.get(p) for p in proxy_vars if os.environ.get(p)}
    return proxies

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False

def detect_ssl_interference():
    try:
        result = subprocess.run(
            ["python", "-m", "pip", "install", "requests"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if "SSL" in result.stderr:
            return True
        return False
    except:
        return False
