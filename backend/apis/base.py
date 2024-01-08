from fastapi import APIRouter

from backend.apis.v1 import route_blog, route_login, route_user

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_blog.router, prefix="", tags=["blogs"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
