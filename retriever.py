import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")

def load_docs():
    docs = []

    if not os.path.exists(KNOWLEDGE_DIR):
        return []

    for file in os.listdir(KNOWLEDGE_DIR):
        with open(os.path.join(KNOWLEDGE_DIR, file), "r", encoding="utf-8") as f:
            docs.append(f.read())

    return docs


def retrieve_context(query):
    docs = load_docs()
    relevant = []

    for doc in docs:
        if any(word in doc.lower() for word in query.lower().split()):
            relevant.append(doc)

    return "\n".join(relevant[:2])