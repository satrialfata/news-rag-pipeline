from src.embedding.embedding_model import get_embedding_model
from src.vectorstore.pinecone_store import get_index


def retrieve(query, top_k=3):

    embedding_model = get_embedding_model()

    index = get_index()

    query_vector = embedding_model.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return results.matches