import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URI")

if not MONGO_URL:
    raise ValueError("MONGO_URI não foi definida no .env")

ENV: dict[str, str | None] = {
    "MONGO_URL": MONGO_URL
}