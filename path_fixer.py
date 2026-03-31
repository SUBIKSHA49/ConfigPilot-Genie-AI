import os
import subprocess
import ctypes

def open_env_vars():
    subprocess.run(
        "rundll32 sysdm.cpl,EditEnvironmentVariables",
        shell=True
    )

def suggest_path_fix(software, bin_path):
    message = f"""
{software.upper()} PATH is missing.

Steps to fix:
1. Click 'New'
2. Paste this path:
{bin_path}
3. Click OK
4. Restart terminal

Do you want me to open Environment Variables now?
"""

    response = ctypes.windll.user32.MessageBoxW(
        0,
        message,
        "PATH Fix Assistant",
        0x04 | 0x40  # YES / NO
    )

    if response == 6:  # YES
        open_env_vars()
