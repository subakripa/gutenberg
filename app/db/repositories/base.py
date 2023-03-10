from asyncpg import Record
from typing import Any
from asyncpg.connection import Connection

class PGSQLBaseRepository:
    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    @property
    def connection(self) -> Connection:
        return self._conn
    
    async def _fetch_row(self, query: str, *query_params: Any) -> Record:
        return await self._conn.fetchrow(query, *query_params)