import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from src.config import ENV

from models import SuaClasseModelo

async def init_db():
    client = AsyncIOMotorClient(ENV["MONGO_URL"])

    # Inicializa o beanie com o banco de dados e os documentos
    await init_beanie(database=client.db_name, document_models=[SuaClasseModelo])

# asyncio.run(init_db()) # Para scripts síncronos, se necessário
