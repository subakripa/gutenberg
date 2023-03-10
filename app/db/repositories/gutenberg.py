from asyncpg.connection import Connection

from app.db.repositories.base import PGSQLBaseRepository

FETCH_BOOKS_QUERY = """
"""

class BooksPGRepository(PGSQLBaseRepository):
    def __init__(self, conn: Connection):
        super().__init__(conn)

    async def get_books_list(self,
                             query_parms: dict 
                             )-> list:
        # async with self.connection.transaction():
        #     books_row = await self._fetch_row(
        #         FETCH_BOOKS_QUERY,
        #         query_parms
        #     )
        #     resp_list= [{k: v for (k, v) in dict(row).items()} for row in books_row]
            return ["resp_list"]