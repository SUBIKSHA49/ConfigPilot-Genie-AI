import os

COMMON_RESIDUAL_PATHS = [
    "C:\\Program Files",
    "C:\\Program Files (x86)",
    "C:\\Users",
    "C:\\ProgramData"
]

def find_residuals(residual_keywords):
    found = []

    for base in COMMON_RESIDUAL_PATHS:
        if not os.path.exists(base):
            continue

        try:
            for item in os.listdir(base):
                full_path = os.path.join(base, item)

                for keyword in residual_keywords:
                    if keyword.lower() in item.lower():
                        found.append(full_path)
                        break

        except PermissionError:
            continue

    return list(set(found))
