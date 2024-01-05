from apis.core.config import settings
from apis.db.base import Base
from apis.db.session import db_engine
from fastapi import FastAPI


def create_tables():
    Base.metadata.create_all(bind=db_engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )  # noqa: E501
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello():
    return {"msg": "Hello world!"}
