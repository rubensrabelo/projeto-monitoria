from beanie import EmbeddedModel
from typing import Union

SQLValue = Union[str, int, float, bool, None]


class Answer(EmbeddedModel):
    columns: list[str]
    rows: list[list[SQLValue]]
    execution_time: float | None = None