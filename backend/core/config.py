import os


class Settings:
    PROJECT_NAME = "Blog app"
    PROJECT_VERSION = "0.1.0"

    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST", "db")
    DB_NAME = os.environ.get("DB_NAME", "blog-app-db")
    DB_PORT = os.environ.get("DB_PORT", "3306")
    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8"  # noqa: E501
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"  # noqa: E501

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
