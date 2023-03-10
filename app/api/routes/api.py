from fastapi import APIRouter

from app.api.routes import (
    gutenberg
)

router = APIRouter()
router.include_router(gutenberg.router, tags=["Book Search"], prefix="/v1")