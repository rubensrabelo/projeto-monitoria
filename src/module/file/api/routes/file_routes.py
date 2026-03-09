from fastapi import APIRouter, UploadFile
from src.module.file.application.services import FileService

router = APIRouter()
service = FileService()


@router.post("/upload")
def upload_file(file: UploadFile):

    table = service.save_dataset(file)

    return {
        "dataset": table
    }
