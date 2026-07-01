from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.category import Category
from src.repositories.category_repository import CategoryRepository
from src.schemas.category_schema import CategoryCreate, CategoryResponse, CategoryUpdate


class CategoryService:

    def __init__(self, db: Session) -> None:
        self.repository = CategoryRepository(db)

    def get_all(self) -> list[CategoryResponse]:
        return self.repository.get_all()

    def get_by_id(self, category_id: int) -> Category:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found.",
            )
        return category

    def create(self, data: CategoryCreate) -> CategoryResponse:
        existing = self.repository.get_by_name(data.name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Category '{data.name}' already exists.",
            )
        return self.repository.create(data)

    def update(self, category_id: int, data: CategoryUpdate) -> CategoryResponse:
        category = self.get_by_id(category_id)

        if data.name:
            existing = self.repository.get_by_name(data.name)
            if existing and existing.id != category_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Category '{data.name}' already exists.",
                )

        return self.repository.update(category, data)

    def delete(self, category_id: int) -> None:
        category = self.get_by_id(category_id)
        self.repository.delete(category)
