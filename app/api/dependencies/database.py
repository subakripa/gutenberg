from typing import AsyncGenerator, Callable, Type

from asyncpg.pool import Pool
from fastapi import Depends
from app.db.events import pgsql_db
from starlette.requests import Request
from app.db.repositories.base import PGSQLBaseRepository

def _get_db_pool(request: Request) -> Pool:
    return request.app.state.pool

def get_pgsql_repository(repo_type: Type[PGSQLBaseRepository]) -> Callable:  # type: ignore
    async def _get_repo(
        pool: Pool = Depends(_get_db_pool),
    ) -> AsyncGenerator[PGSQLBaseRepository, None]:
        async with pool.acquire() as conn:
            yield repo_type(conn)

    return _get_repo