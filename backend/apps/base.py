from fastapi import APIRouter

from backend.apps.v1 import route_blog, route_login

app_router = APIRouter()

app_router.include_router(
    route_blog.router, prefix="", tags=[""], include_in_schema=False
)
app_router.include_router(
    route_login.router, prefix="/auth", tags=[""], include_in_schema=False
)
