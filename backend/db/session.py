from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
db_engine = create_engine(SQLALCHEMY_DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def get_db() -> Generator:
    with db_session() as session:
        yield session
