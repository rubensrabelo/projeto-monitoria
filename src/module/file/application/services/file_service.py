import os
from src.infra.db import duckdb_manager

DATASET_PATH = "datasets"


class FileService:

    def save_dataset(self, file):

        path = os.path.join(DATASET_PATH, file.filename)

        with open(path, "wb") as f:
            f.write(file.file.read())

        table_name = file.filename.replace(".csv", "")

        duckdb_manager.register_csv(table_name, path)

        return table_name
