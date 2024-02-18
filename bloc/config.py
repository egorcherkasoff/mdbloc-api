from dotenv import load_dotenv
from os import environ

load_dotenv()


class AppConfig:
    """Содержит настройки приложения"""

    MONGO_URL = environ.get("MONGO_URL")
    MONGO_PORT = environ.get("MONGO_PORT")
    MONGO_USER = environ.get("MONGO_INITDB_ROOT_USERNAME")
    MONGO_PASS = environ.get("MONGO_INITDB_ROOT_PASSWORD")
    MONGO_DB_NAME = environ.get("MONGO_INITDB_DATABASE")
    JWT_SECRET = environ.get("JWT_SECRET")
