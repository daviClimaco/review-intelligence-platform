from fastapi import FastAPI
from src.api.routers.author_router import router as author_router

app = FastAPI(
    title="Review Intelligence Platform",
    version="1.0.0"
)

app.include_router(author_router)

@app.get("/")
def root():
    return {
        "message": "Review Intelligence Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }
