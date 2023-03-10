from fastapi import Depends, Query
from typing import List
from app.api.dependencies.database import get_pgsql_repository
from app.db.repositories.gutenberg import BooksPGRepository

async def search_books_dependency(
    book_id: List[int] = Query(default=None),
    language: List[str] = Query(default=None),
    mime_type: List[str] = Query(default=None),
    topic: List[str] = Query(default=None),
    author: List[str] = Query(default=None),
    title: List[str] = Query(default=None),
    books_repo : BooksPGRepository = Depends(get_pgsql_repository(BooksPGRepository))
) -> List:
    """
    Method that queries the PSQL DB for Books search. Serves the end point /project.book-search.
    All of the parameters are optional.

    Returns:
        List: List containing JSON objects. Each object is a book matching the filter criteria.
    """
    try:
        query_parms = dict()
        if book_id:
            query_parms['book_id'] = book_id
        if language:
            query_parms['language'] = language
        if mime_type:
            query_parms['mime_type'] = mime_type
        if topic:
            query_parms['topic'] = [x.lower() for x in topic]
        if author:
            query_parms['author'] = [y.lower() for y in author]
        if title:
            query_parms['title'] = [z.lower() for z in title]
        return await books_repo.get_books_list(
            query_parms
        )
    except Exception:
        raise