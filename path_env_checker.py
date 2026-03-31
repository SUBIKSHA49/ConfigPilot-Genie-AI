import os

def get_path_entries():
    """
    Returns list of PATH entries (user + system combined)
    """
    path_value = os.environ.get("PATH", "")
    return [p.strip() for p in path_value.split(";") if p.strip()]


def check_path_env(bin_paths):
    """
    bin_paths: list of expected bin directories
    returns: dict with missing and present paths
    """
    env_paths = get_path_entries()

    present = []
    missing = []

    for path in bin_paths:
        expanded = os.path.expandvars(path)

        if expanded in env_paths:
            present.append(expanded)
        else:
            missing.append(expanded)

    return {
        "present": present,
        "missing": missing
    }
