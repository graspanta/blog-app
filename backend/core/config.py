import os


class Settings:
    PROJECT_NAME = "Blog app"
    PROJECT_VERSION = "0.1.0"

    DATABASE_URL = "mysql+pymysql://root@db:3306/blog-app-db?charset=utf8"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
