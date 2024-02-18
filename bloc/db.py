from beanie import init_beanie
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bloc.config import AppConfig


from bloc.models import Comment, User, Publication


async def init():
    """создает клиент motor и загружает модели в бд"""
    client = AsyncIOMotorClient(
        f"mongodb://{AppConfig.MONGO_USER}:{AppConfig.MONGO_PASS}@{AppConfig.MONGO_URL}:{AppConfig.MONGO_PORT}",
        uuidRepresentation="standard",
    )
    db = client[AppConfig.MONGO_DB_NAME]
    await init_beanie(
        database=db,
        document_models=[
            User,
            Publication,
            Comment,
        ],
    )
