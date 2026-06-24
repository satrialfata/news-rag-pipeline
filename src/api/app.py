from fastapi import FastAPI
from pydantic import BaseModel

from src.pipeline import run_pipeline
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


@app.post("/update-news")
def update_news():

    run_pipeline()

    return {
        "message": "News updated successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }