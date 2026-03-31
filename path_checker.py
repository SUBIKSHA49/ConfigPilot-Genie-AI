import subprocess
import os

# -------------------------------------------------
# 🔹 Check if binary is available in PATH
# -------------------------------------------------
def check_binary(binary):
    try:
        result = subprocess.run(
            ["where", binary],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )

        if result.returncode == 0:
            return {
                "found": True,
                "locations": result.stdout.strip().splitlines()
            }
        else:
            return {
                "found": False,
                "error": result.stderr.strip()
            }

    except Exception as e:
        return {"found": False, "exception": str(e)}


# -------------------------------------------------
# 🔹 Check for multiple binaries (conflicts)
# -------------------------------------------------
def check_path_conflicts(binary):
    result = check_binary(binary)

    if result["found"] and len(result["locations"]) > 1:
        return {
            "conflict": True,
            "details": result["locations"]
        }

    return {"conflict": False}


# -------------------------------------------------
# 🔹 Get PATH entries
# -------------------------------------------------
def get_path_entries():
    return os.environ.get("PATH", "").split(";")


# -------------------------------------------------
# 🔥 NEW: Check manual install locations
# (detect installed but not in PATH)
# -------------------------------------------------
def check_manual_paths(bin_paths, binary_name):
    found_paths = []

    for path in bin_paths:
        full_path = os.path.join(path, binary_name)

        # Windows executable extension
        if os.name == "nt":
            full_path += ".exe"

        if os.path.exists(full_path):
            found_paths.append(full_path)

    return found_paths