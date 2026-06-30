from fastapi import APIRouter

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)


@router.get("/")
def get_authors():
    return {
        "message": "Lista de autores"
    }
