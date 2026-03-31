def reason(facts):
    """
    facts: dict produced by inspectors
    returns: reasoning + actions
    """

    conclusions = []
    actions = []

    binary_info = facts.get("binary_found", {})
    binary_exists = binary_info.get("found", False)

    # ---------- PATH ISSUES ----------
    if not binary_exists and facts.get("install_found"):
        conclusions.append(
            f"{facts['software']} is installed but not accessible from terminal"
        )
        actions.append(
            "Add installation directory to PATH environment variable"
        )

    # ---------- NOT INSTALLED ----------
    if not facts.get("install_found") and not binary_exists:
        conclusions.append(
            f"{facts['software']} is not installed"
        )
        actions.append(
            f"Download and install {facts['software']} from the official website"
        )

    # ---------- RESIDUAL FILES ----------
    if facts.get("residuals"):
        conclusions.append(
            "Residual files detected from previous installation"
        )
        actions.append(
            "Remove residual folders and reinstall cleanly"
        )

    # ---------- NETWORK ISSUES ----------
    if facts.get("proxy_enabled") and not facts.get("internet_available"):
        conclusions.append(
            "Network or proxy settings may block installation"
        )
        actions.append(
            "Disable proxy/firewall temporarily and retry installation"
        )

    # ---------- HEALTHY STATE ----------
    if not conclusions and not actions:
        conclusions.append(
            f"{facts['software']} installation looks healthy"
        )
        actions.append(
            "No action required"
        )

    return {
        "conclusions": conclusions,
        "recommended_actions": actions
    }
