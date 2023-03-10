from fastapi import APIRouter, Depends
from app.api.dependencies.gutenberg import search_books_dependency
from starlette.status import HTTP_200_OK
router = APIRouter()

@router.get(
    "/project.book-search",
    status_code=HTTP_200_OK,
    name="search:get-books"
)
async def get_searched_books(books_list: list = Depends(search_books_dependency))-> list:
    """
    Method that gest invoked on /project.book-search. It depends on successful DB connection
    and proper parameter passing. If not an error is raised.

    Returns:
        list: List of Books fetched from DB.
    """
    return books_list