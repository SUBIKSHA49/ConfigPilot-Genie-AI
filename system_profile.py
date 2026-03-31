import platform
import subprocess
import sys

def collect_system_profile():
    profile = {}

    # Python version
    profile["python_version"] = platform.python_version()

    # OS
    profile["os"] = platform.system()

    # Try detecting GPU (simple version)
    try:
        out = subprocess.check_output(
            "nvidia-smi",
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode()
        profile["gpu_present"] = True
    except:
        profile["gpu_present"] = False

    return profile