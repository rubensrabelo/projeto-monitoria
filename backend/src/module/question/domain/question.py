from beanie import Document
from datetime import datetime, timezone

from answer import Answer


class Question(Document):
    question: str
    sql: str
    dataset: str

    answer: Answer | None = None

    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)

    class Settings:
        name = "questions"

    async def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return await super().save(*args, **kwargs)
