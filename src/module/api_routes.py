from fastapi import APIRouter

from .file.api.routes import file_routes
from .query.api.routes import query_routes

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(
    file_routes,
    prefix="/files",
    tags=["File"]
)

api_v1_router.include_router(
    query_routes,
    prefix="/queries",
    tags=["Query"]
)
