import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

from src.services.author_service import AuthorService
from src.schemas.author_schema import AuthorCreate


# instead of instantiating the real Author model (which triggers SQLAlchemy),
# we use MagicMock to simulate the object - the service only calls attributes,
# so a mock works perfectly here
def make_author(id=1, name="Test Author"):
    author = MagicMock()
    author.id = id
    author.name = name
    return author


def make_service():
    mock_db = MagicMock()
    return AuthorService(mock_db)


class TestGetById:

    def test_returns_author_when_found(self):
        service = make_service()
        fake_author = make_author()

        service.repository.get_by_id = MagicMock(return_value=fake_author)

        result = service.get_by_id(1)
        assert result.name == "Test Author"

    def test_raises_404_when_not_found(self):
        service = make_service()

        service.repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.get_by_id(999)

        assert exc.value.status_code == 404


class TestCreate:

    def test_creates_author_successfully(self):
        service = make_service()
        fake_author = make_author(name="New Author")

        service.repository.create = MagicMock(return_value=fake_author)

        data = AuthorCreate(name="New Author")
        result = service.create(data)

        assert result.name == "New Author"
        service.repository.create.assert_called_once_with(data)


class TestDelete:

    def test_raises_404_when_author_not_found(self):
        service = make_service()
        service.repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.delete(999)

        assert exc.value.status_code == 404

    def test_deletes_successfully(self):
        service = make_service()
        fake_author = make_author()

        service.repository.get_by_id = MagicMock(return_value=fake_author)
        service.repository.delete = MagicMock()

        service.delete(1)

        service.repository.delete.assert_called_once_with(fake_author)
