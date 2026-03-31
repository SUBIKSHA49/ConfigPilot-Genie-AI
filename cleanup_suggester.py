import os
import ctypes

def suggest_cleanup(residual_paths):
    if not residual_paths:
        return

    count = len(residual_paths)

    preview = "\n".join(residual_paths[:5])
    more = f"\n... and {count - 5} more" if count > 5 else ""

    message = f"""
{count} residual folders were detected.

Examples:
{preview}{more}

Recommendation:
- Delete these folders if software is not working
- Reinstall cleanly afterwards

Do you want me to open these locations now?
"""

    response = ctypes.windll.user32.MessageBoxW(
        0,
        message,
        "Residual Cleanup Assistant",
        0x04 | 0x40  # YES / NO
    )

    if response == 6:  # YES
        for path in residual_paths:
            if os.path.exists(path):
                os.startfile(path)
