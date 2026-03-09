from src.infra.db import duckdb_manager


class QueryService:

    def run(self, query: str):

        query_upper = query.upper()

        if not query_upper.startswith("SELECT"):
            raise Exception("Somente SELECT permitido")

        result = duckdb_manager.run_query(query)

        return result
