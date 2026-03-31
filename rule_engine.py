def reason(facts, rule=None):
    conclusions = []
    actions = []

    software = facts.get("software")
    install_found = facts.get("install_found")

    # binary may be dict or bool
    binary_info = facts.get("binary_found", {})
    binary_found = (
        binary_info.get("found")
        if isinstance(binary_info, dict)
        else bool(binary_info)
    )

    # PATH environment info
    path_env = facts.get("path_env", {})
    missing_paths = path_env.get("missing", [])

    # =====================================================
    # 1️⃣ PRIORITY CASE — PATH MISCONFIGURED
    # =====================================================
    if install_found and missing_paths:
        conclusions.append(
            f"{software} is installed but PATH is not configured correctly"
        )

        actions.append(
            "Add the software's bin directory to PATH environment variable"
        )
        actions.append(
            "Open Environment Variables → Edit PATH → Add new entry"
        )
        actions.append(
            "Restart terminal after updating PATH"
        )

        # STOP reasoning here (important design choice)
        return {
            "conclusions": conclusions,
            "recommended_actions": actions
        }

    # =====================================================
    # 2️⃣ NOT INSTALLED → SMART INSTALL ADVISOR
    # =====================================================
    if not install_found:
        conclusions.append(f"{software} is not installed")

        if rule:
            url = rule.get("download_url")
            version = rule.get("recommended_version")
            notes = rule.get("install_notes")

            if url:
                actions.append(f"Download from official site: {url}")
            else:
                actions.append(
                    f"Download {software} from its official website"
                )

            if version:
                actions.append(
                    f"Recommended version to install: {version}"
                )

            if notes:
                actions.append(
                    f"Why this version: {notes}"
                )

        else:
            actions.append(
                f"Install {software} from its official website"
            )

        return {
            "conclusions": conclusions,
            "recommended_actions": actions
        }

    # =====================================================
    # 3️⃣ RESIDUAL FILES (ONLY AFTER PATH IS OK)
    # =====================================================
    residuals = facts.get("residuals", [])
    if residuals:
        conclusions.append(
            "Residual files from previous installation detected"
        )

        actions.append(
            f"{len(residuals)} residual locations found"
        )
        actions.append(
            "Consider removing them before reinstalling"
        )

    # =====================================================
    # 4️⃣ NETWORK / PROXY ISSUE
    # =====================================================
    if facts.get("proxy_enabled") and not facts.get("internet_available"):
        conclusions.append("Network or proxy issue detected")

        actions.append(
            "Disable proxy or firewall temporarily"
        )
        actions.append(
            "Retry installation after fixing network"
        )

    # =====================================================
    # 5️⃣ ALL GOOD CASE (VERY IMPORTANT)
    # =====================================================
    if not conclusions:
        conclusions.append(
            f"{software} appears correctly installed and configured"
        )
        actions.append(
            "No action needed"
        )

    return {
        "conclusions": conclusions,
        "recommended_actions": actions
    }