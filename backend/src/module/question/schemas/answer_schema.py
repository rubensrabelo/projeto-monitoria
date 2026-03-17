from pydantic import BaseModel
from typing import Union

SQLValue = Union[str, int, float, bool, None]


class AnswerSchema(BaseModel):
    columns: list[str]
    rows: list[list[SQLValue]]
    execution_time: float | None = None
