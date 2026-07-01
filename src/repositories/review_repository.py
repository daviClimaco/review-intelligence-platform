from sqlalchemy.orm import Session

from src.models.review import Review
from src.schemas.review_schema import ReviewCreate, ReviewUpdate


class ReviewRepository:

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Review]:
        return self.db.query(Review).order_by(Review.id).all()

    def get_by_id(self, review_id: int) -> Review | None:
        return self.db.query(Review).filter(Review.id == review_id).first()

    def get_by_author(self, author_id: int) -> list[Review]:
        return (
            self.db.query(Review)
            .filter(Review.author_id == author_id)
            .order_by(Review.id)
            .all()
        )

    def get_by_category(self, category_id: int) -> list[Review]:
        return (
            self.db.query(Review)
            .filter(Review.category_id == category_id)
            .order_by(Review.id)
            .all()
        )

    def create(self, data: ReviewCreate) -> Review:
        review = Review(**data.model_dump())
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def update(self, review: Review, data: ReviewUpdate) -> Review:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(review, field, value)
        self.db.commit()
        self.db.refresh(review)
        return review

    def delete(self, review: Review) -> None:
        self.db.delete(review)
        self.db.commit()
