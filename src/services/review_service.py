from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.review import Review
from src.repositories.author_repository import AuthorRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.review_repository import ReviewRepository
from src.schemas.review_schema import ReviewCreate, ReviewResponse, ReviewUpdate


class ReviewService:

    def __init__(self, db: Session) -> None:
        self.repository = ReviewRepository(db)
        self.author_repository = AuthorRepository(db)
        self.category_repository = CategoryRepository(db)

    def _validate_author(self, author_id: int) -> None:
        if not self.author_repository.get_by_id(author_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Author with id {author_id} not found.",
            )

    def _validate_category(self, category_id: int) -> None:
        if not self.category_repository.get_by_id(category_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found.",
            )

    def get_all(self) -> list[ReviewResponse]:
        return self.repository.get_all()

    def get_by_id(self, review_id: int) -> Review:
        review = self.repository.get_by_id(review_id)
        if not review:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Review with id {review_id} not found.",
            )
        return review

    def get_by_author(self, author_id: int) -> list[ReviewResponse]:
        self._validate_author(author_id)
        return self.repository.get_by_author(author_id)

    def get_by_category(self, category_id: int) -> list[ReviewResponse]:
        self._validate_category(category_id)
        return self.repository.get_by_category(category_id)

    def create(self, data: ReviewCreate) -> ReviewResponse:
        self._validate_author(data.author_id)
        self._validate_category(data.category_id)
        return self.repository.create(data)

    def update(self, review_id: int, data: ReviewUpdate) -> ReviewResponse:
        review = self.get_by_id(review_id)
        return self.repository.update(review, data)

    def delete(self, review_id: int) -> None:
        review = self.get_by_id(review_id)
        self.repository.delete(review)
