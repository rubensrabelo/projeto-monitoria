from pydantic import BaseModel
from datetime import datetime

from schemas import AnswerSchema

class QuestionResponse(BaseModel):
    id: str
    question: str
    sql: str
    dataset: str
    answer: AnswerSchema | None
    created_at: datetime
    updated_at: datetime