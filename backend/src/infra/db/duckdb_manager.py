import duckdb


class DuckDBManager:

    def __init__(self):
        self.con = duckdb.connect()

    def register_csv(self, table_name: str, path: str):

        query = f"""
        CREATE OR REPLACE VIEW {table_name} AS
        SELECT *
        FROM read_csv_auto('{path}')
        """

        self.con.execute(query)

    def run_query(self, query: str):
        return self.con.execute(query).fetchall()


duckdb_manager = DuckDBManager()
