from inspector.inspector_runner import inspect
from reasoner.rule_engine import reason
from fixer.path_fixer import suggest_path_fix
from fixer.cleanup_suggester import suggest_cleanup

from rag.retriever import retrieve_context
from llm.prompt_builder import build_prompt
from llm.gemini_client import get_llm_response


def run_agent(software):
    # ----------------------------
    # Step 1: Inspect system
    # ----------------------------
    facts = inspect(software)

    if "error" in facts:
        print("\n", facts["error"])
        return

    # ----------------------------
    # Step 2: Rule-based reasoning
    # ----------------------------
    analysis = reason(facts)

    print("\n=== Personal AI System Inspector ===\n")

    print("\n--- FACTS ---")
    for k, v in facts.items():
        print(f"{k}: {v}")

    print("\n--- RULE-BASED REASONING ---")
    for c in analysis["conclusions"]:
        print("•", c)

    print("\n--- RULE-BASED ACTIONS ---")
    for a in analysis["recommended_actions"]:
        print("→", a)

    # ----------------------------
    # Step 3: Fixer Logic
    # ----------------------------
    actions_text = " ".join(analysis["recommended_actions"]).lower()

    # PATH Fix
    if "path" in actions_text:
        bin_paths = facts.get("bin_paths", [])

        if bin_paths:
            suggest_path_fix(software, bin_paths)
        else:
            print("\nNo bin paths detected to fix PATH.")

    # Residual Cleanup
    if facts.get("residuals"):
        suggest_cleanup(facts["residuals"])

    # ----------------------------
    # Step 4: RAG + LLM (Gemini)
    # ----------------------------
    print("\n--- AI RECOMMENDATION (LLM + RAG) ---\n")

    query = f"{software} installation compatibility best version"
    context = retrieve_context(query)

    prompt = build_prompt(facts, context, software)

    response = get_llm_response(prompt)

    print(response)


# ----------------------------
# MAIN ENTRY
# ----------------------------
if __name__ == "__main__":
    software = input(
        "\nEnter software name (python / java / git / docker / cuda / node / angular): "
    ).strip().lower()

    run_agent(software)