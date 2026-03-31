import os

def detect_installation(info, binary_result=None):
    """
    info: software config dict
    binary_result: output from check_binary()
    """

    # If binary is found, software is installed
    if binary_result and binary_result.get("found"):
        return True

    # Fallback: check known install paths
    install_paths = info.get("install_paths", [])

    for path in install_paths:
        # Expand %USERNAME% if present
        expanded_path = os.path.expandvars(path)

        if os.path.exists(expanded_path):
            return True

    return False
