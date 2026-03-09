from odmantic import Model, EmbeddedModel
from datetime import datetime, timezone
from typing import Any
from pydantic import Field


class Answer(EmbeddedModel):
    columns: list[str]
    rows: list[list[Any]]
    execution_time: float | None = None


class Question(Model):
    question: str
    sql: str
    dataset: str

    answer: Answer | None = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
