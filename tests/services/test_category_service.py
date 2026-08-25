import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

from src.services.category_service import CategoryService
from src.schemas.category_schema import CategoryCreate


def make_category(id=1, name="Test Category"):
    category = MagicMock()
    category.id = id
    category.name = name
    return category


def make_service():
    mock_db = MagicMock()
    return CategoryService(mock_db)


class TestGetById:

    def test_returns_category_when_found(self):
        service = make_service()
        service.repository.get_by_id = MagicMock(return_value=make_category())

        result = service.get_by_id(1)
        assert result.name == "Test Category"

    def test_raises_404_when_not_found(self):
        service = make_service()
        service.repository.get_by_id = MagicMock(return_value=None)

        with pytest.raises(HTTPException) as exc:
            service.get_by_id(999)

        assert exc.value.status_code == 404


class TestCreate:

    def test_creates_category_successfully(self):
        service = make_service()

        # no duplicate found
        service.repository.get_by_name = MagicMock(return_value=None)
        service.repository.create = MagicMock(return_value=make_category(name="Atendimento"))

        result = service.create(CategoryCreate(name="Atendimento"))
        assert result.name == "Atendimento"

    def test_raises_409_when_name_already_exists(self):
        service = make_service()

        # simulate duplicate found in database
        service.repository.get_by_name = MagicMock(return_value=make_category())

        with pytest.raises(HTTPException) as exc:
            service.create(CategoryCreate(name="Test Category"))

        assert exc.value.status_code == 409
