import os

def detect_cuda_installation(rule, binary_result=None):
    """
    Detect CUDA installation using multiple strategies
    """

    # 1️⃣ PATH detection (nvcc)
    if binary_result and isinstance(binary_result, dict):
        if binary_result.get("found"):
            return True

    # 2️⃣ Default install folder check
    possible_paths = [
        r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA",
        r"C:\CUDA"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return True

    return False