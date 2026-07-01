from fastapi import FastAPI

from src.api.routers.author_router import router as author_router
from src.api.routers.category_router import router as category_router
from src.api.routers.review_router import router as review_router

app = FastAPI(
    title="Review Intelligence Platform",
    version="1.0.0",
    description="End-to-end review intelligence platform for collecting, managing and analyzing customer reviews.",
)

app.include_router(author_router)
app.include_router(category_router)
app.include_router(review_router)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Review Intelligence Platform API"}


@app.get("/health", tags=["Root"])
def health():
    return {"status": "OK"}
