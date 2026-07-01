from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.api.routers.dependencies import get_db
from src.schemas.review_schema import ReviewCreate, ReviewResponse, ReviewUpdate
from src.services.review_service import ReviewService

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"],
)


@router.get("/", response_model=list[ReviewResponse])
def get_all_reviews(db: Session = Depends(get_db)):
    return ReviewService(db).get_all()


@router.get("/{review_id}", response_model=ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    return ReviewService(db).get_by_id(review_id)


@router.get("/by-author/{author_id}", response_model=list[ReviewResponse])
def get_reviews_by_author(author_id: int, db: Session = Depends(get_db)):
    return ReviewService(db).get_by_author(author_id)


@router.get("/by-category/{category_id}", response_model=list[ReviewResponse])
def get_reviews_by_category(category_id: int, db: Session = Depends(get_db)):
    return ReviewService(db).get_by_category(category_id)


@router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
def create_review(data: ReviewCreate, db: Session = Depends(get_db)):
    return ReviewService(db).create(data)


@router.put("/{review_id}", response_model=ReviewResponse)
def update_review(review_id: int, data: ReviewUpdate, db: Session = Depends(get_db)):
    return ReviewService(db).update(review_id, data)


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    ReviewService(db).delete(review_id)
