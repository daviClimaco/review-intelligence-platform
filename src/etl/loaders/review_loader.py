from sqlalchemy.orm import Session

from src.repositories.author_repository import AuthorRepository
from src.repositories.category_repository import CategoryRepository
from src.repositories.review_repository import ReviewRepository
from src.schemas.author_schema import AuthorCreate
from src.schemas.category_schema import CategoryCreate
from src.schemas.review_schema import ReviewCreate


class ReviewLoader:

    def __init__(self, db: Session) -> None:
        self.author_repo = AuthorRepository(db)
        self.category_repo = CategoryRepository(db)
        self.review_repo = ReviewRepository(db)

    def _get_or_create_author(self, name: str):
        # reuse existing author or create a new one
        author = self.author_repo.get_by_name(name)
        if not author:
            author = self.author_repo.create(AuthorCreate(name=name))
        return author

    def _get_or_create_category(self, name: str):
        # reuse existing category or create a new one
        category = self.category_repo.get_by_name(name)
        if not category:
            category = self.category_repo.create(CategoryCreate(name=name))
        return category

    def load(self, rows: list[dict]) -> None:
        loaded = 0

        for row in rows:
            author = self._get_or_create_author(row["author_name"])
            category = self._get_or_create_category(row["category_name"])

            self.review_repo.create(ReviewCreate(
                author_id=author.id,
                category_id=category.id,
                rating=row["rating"],
                review_text=row["review_text"],
                sentiment=row["sentiment"],
                platform=row["platform"],
                review_date=row["review_date"],
            ))
            loaded += 1

        print(f"[Loader] {loaded} reviews saved to database")
