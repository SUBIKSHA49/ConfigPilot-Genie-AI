def build_prompt(facts, context, software):
    return f"""
You are an expert system configuration assistant.

System Information:
{facts}

Knowledge Base:
{context}

User wants to install: {software}

Tasks:
1. Suggest BEST compatible version (optimized, stable)
2. Consider OS, GPU, Python version
3. Avoid unstable/latest-breaking versions
4. Give step-by-step installation guide

Output format:
- Recommended Version
- Reason
- Steps to Install
"""