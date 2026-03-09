from fastapi import APIRouter
from src.module.query.schemas import SQLQuery
from src.module.query.application.services import QueryService

router = APIRouter()
service = QueryService()


@router.post("/")
def run_query(body: SQLQuery):

    result = service.run(body.query)

    return {
        "rows": result
    }
