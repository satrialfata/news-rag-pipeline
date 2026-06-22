from fastapi import FastAPI
from pydantic import BaseModel

from src.chains.rag_chain import ask

app = FastAPI(
    title="News RAG API",
    description="News Retrieval Augmented Generation API",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "News RAG API Running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask(request.question)

    return {
        "question": request.question,
        "answer": answer
    }