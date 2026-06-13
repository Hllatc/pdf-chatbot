def build_prompt(context: str, question: str):

    return f"""
You are an AI assistant for answering questions about uploaded PDF documents.

Rules:
- Answer only using the provided context.
- If the answer is not in the context, say:
  "I couldn't find that information in the PDF."
- Keep the answer concise and accurate.

Context:
{context}

Question:
{question}

Answer:
"""