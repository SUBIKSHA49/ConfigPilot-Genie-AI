from rules.rule_loader import load_rules
from .path_checker import check_binary, check_path_conflicts, check_manual_paths
from .install_detector import detect_installation
from .residual_detector import find_residuals
from .network_security_detector import detect_proxy, check_internet
from .path_env_checker import check_path_env
from .system_profile import collect_system_profile

RULES = load_rules()

def inspect(software_name):
    rule = RULES.get(software_name)

    if not rule:
        # 🔥 fallback generic detection
        binary_result = check_binary(software_name)

        return {
            "software": software_name,
            "binary_found": binary_result,
            "note": "No predefined rules. Basic detection applied."
        }

    # ----------------------------
    # Extract reusable values
    # ----------------------------
    binary_name = rule["binary"]
    bin_paths = rule.get("bin_paths", [])

    # ----------------------------
    # Run core checks
    # ----------------------------
    binary_result = check_binary(binary_name)
    install_found = detect_installation(rule, binary_result)

    # ----------------------------
    # 🔥 GENERIC PATH PROPAGATION CHECK
    # ----------------------------
    manual_paths = check_manual_paths(bin_paths, binary_name)

    if binary_result:
        path_status = "working"

    elif manual_paths:
        path_status = "installed_but_not_in_path"

    else:
        path_status = "not_installed"

    # ----------------------------
    # Residual scan only when useful
    # ----------------------------
    residuals = []
    if path_status == "not_installed":
        residuals = find_residuals(rule.get("residual_keywords", []))

    # ----------------------------
    # Network checks only if install missing
    # ----------------------------
    proxy_enabled = {}
    internet_available = True

    if path_status == "not_installed":
        proxy_enabled = detect_proxy()
        internet_available = check_internet()

    # ----------------------------
    # Build fact dictionary
    # ----------------------------
    facts = {
        "software": software_name,
        "binary_found": binary_result,
        "install_found": install_found,
        "path_status": path_status,                 # 🔥 KEY FIELD
        "manual_detected_paths": manual_paths,      # 🔥 KEY FIELD
        "path_conflict": check_path_conflicts(binary_name),
        "residuals": residuals,
        "proxy_enabled": proxy_enabled,
        "internet_available": internet_available,
        "bin_paths": bin_paths,
        "path_env": check_path_env(bin_paths),
        "system_profile": collect_system_profile()
    }

    return facts