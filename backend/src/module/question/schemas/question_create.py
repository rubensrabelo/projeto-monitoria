from pydantic import BaseModel
from datetime import datetime


class QuestionCreate(BaseModel):
    question: str
    sql: str
    dataset: str
