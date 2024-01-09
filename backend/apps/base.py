from fastapi import APIRouter

from backend.apps.v1 import route_blog

app_router = APIRouter()

app_router.include_router(
    route_blog.router, prefix="", tags=[""], include_in_schema=False
)
