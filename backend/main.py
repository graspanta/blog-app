from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.apis.base import api_router
from backend.apps.base import app_router
from backend.core.config import settings
from backend.db.base import Base
from backend.db.session import db_engine


def create_tables():
    Base.metadata.create_all(bind=db_engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount(
        "/static",
        StaticFiles(directory="backend/static"),
        name="static",  # noqa: E501
    )


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )  # noqa: E501
    create_tables()
    include_router(app)
    configure_staticfiles(app)
    return app


app = start_application()


@app.get("/")
def hello():
    return {"msg": "Hello world!"}
