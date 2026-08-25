import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

# import all models first to ensure SQLAlchemy registers them
from src.models.review import Review  # noqa
from src.models.author import Author  # noqa
from src.models.category import Category  # noqa

from src.services.review_service import ReviewService
from src.schemas.review_schema import ReviewCreate


def make_review(id=1, rating=5.0, sentiment="positive"):
    review = MagicMock()
    review.id = id
    review.rating = rating
    review.sentiment = sentiment
    return review


def make_service():
    mock_db = MagicMock()
    return ReviewService(mock_db)


class TestGetById:

    def test_returns_review_when_found(self):
        service = make_service()
        service.repository.get_by_id = MagicMock(return_value=make_review())

        result = service.get_by_id(1)
        assert result.rating == 5.0

    def test_raises_404_when_not_found(self):
        service = make_service()
        service.repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.get_by_id(999)

        assert exc.value.status_code == 404


class TestCreate:

    def test_raises_404_when_author_not_found(self):
        service = make_service()
        service.author_repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.create(ReviewCreate(
                author_id=999,
                category_id=1,
                rating=5.0,
                review_text="Great place!"
            ))

        assert exc.value.status_code == 404

    def test_raises_404_when_category_not_found(self):
        service = make_service()
        service.author_repository.get_by_id = MagicMock(return_value=MagicMock())
        service.category_repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.create(ReviewCreate(
                author_id=1,
                category_id=999,
                rating=5.0,
                review_text="Great place!"
            ))

        assert exc.value.status_code == 404

    def test_creates_review_successfully(self):
        service = make_service()
        service.author_repository.get_by_id = MagicMock(return_value=MagicMock())
        service.category_repository.get_by_id = MagicMock(return_value=MagicMock())
        service.repository.create = MagicMock(return_value=make_review(rating=4.5))

        result = service.create(ReviewCreate(
            author_id=1,
            category_id=1,
            rating=4.5,
            review_text="Great place!"
        ))

        assert result.rating == 4.5
