from src.retrieval.retriever import retrieve
from src.llm.gemini_client import get_llm


def ask(question: str) -> str:

    matches = retrieve(question)

    if not matches:
        return "Tidak ditemukan informasi yang relevan dalam basis pengetahuan."

    context = "\n\n".join(
        [
            f"""
Title: {m.metadata.get('title', '')}
Source: {m.metadata.get('source', '')}

Content:
{m.metadata.get('content', '')}
"""
            for m in matches
        ]
    )

    sources = "\n".join(
        [
            f"- {m.metadata.get('title', '')} ({m.metadata.get('source', '')})"
            for m in matches
        ]
    )

    prompt = f"""
Anda adalah AI News Analyst.

Tugas Anda:
1. Jawab pertanyaan hanya berdasarkan konteks yang diberikan.
2. Jangan membuat informasi yang tidak ada pada konteks.
3. Jika informasi tidak ditemukan, katakan "Informasi tidak ditemukan dalam konteks yang tersedia."
4. Berikan jawaban yang ringkas, jelas, dan mudah dipahami.
5. Setelah jawaban, tampilkan sumber yang digunakan.

KONTEKS:
{context}

PERTANYAAN:
{question}

Format Jawaban:

Jawaban:
<isi jawaban>

Sumber:
<sumber yang digunakan>
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content