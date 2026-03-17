from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.config import ENV
from src.module.question.domain import Question

async def init_db():
    client = AsyncIOMotorClient(ENV["MONGO_URL"])
    db = client.get_database()

    await init_beanie(
        database=db,
        document_models=[Question]
    )
