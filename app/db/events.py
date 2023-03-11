import asyncpg
from asyncpg.pool import Pool
from fastapi import FastAPI
from typing import Callable
from loguru import logger


class PSQLDB:
    client_pool: Pool = None


pgsql_db = PSQLDB()


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to Postgres")

    pool: Pool = await asyncpg.create_pool(
        host="gutenberg.cdxtstm5qxz2.ap-south-1.rds.amazonaws.com",
        port=5432,
        user="postgres",
        password="postgres",
        # database="gutenberg",
        min_size=1,
        max_size=2,
        command_timeout=10,
    )
    app.state.pool = pool
    pgsql_db.client_pool = pool

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")

def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        await connect_to_db(app)

    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app