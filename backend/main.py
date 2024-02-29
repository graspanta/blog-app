from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, text
from sqlalchemy.exc import InternalError, OperationalError

from backend.apis.base import api_router
from backend.apps.base import app_router
from backend.core.config import settings
from backend.db.base import Base
from backend.db.session import db_engine


def database_exists():
    try:
        db_engine.connect()
        return True
    except (OperationalError, InternalError) as e:
        print(e)
        print("Database does not exist")
        return False


def create_tables():
    if not database_exists():
        root = create_engine(settings.DB_URL, echo=True)
        with root.connect() as conn:
            conn.execute(text("CREATE DATABASE `blog-app-db`"))
            print("Database created")
    Base.metadata.create_all(bind=db_engine)
    print("Tables created")


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    app.mount(
        "/static",
        StaticFiles(directory="backend/static"),
        name="static",
    )


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )
    create_tables()
    include_router(app)
    configure_staticfiles(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = start_application()
