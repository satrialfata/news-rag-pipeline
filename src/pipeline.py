from uuid import uuid4

from src.ingestion.news_api import fetch_news
from src.processing.clean_text import clean_text
from src.embedding.embedding_model import get_embedding_model
from src.vectorstore.pinecone_store import get_index


def run_pipeline():

    news = fetch_news()

    embedding_model = get_embedding_model()

    index = get_index()

    vectors = []

    for article in news:

        content = clean_text(
            article.get("content", "")
        )

        if not content:
            continue

        vector = embedding_model.embed_query(
            content
        )

        vectors.append(
    {
        "id": str(uuid4()),
        "values": vector,
        "metadata": {
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"],
            "content": content[:3000]
        }
    }
)

    index.upsert(vectors=vectors)

    print(f"Upload {len(vectors)} artikel selesai")