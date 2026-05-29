import os

import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine

from data.collector.dal.db.postgress.PGConnection import PGConnection
from data.collector.dal.interfaces.TimeReturnsRepo import TimeReturnsRepo


class TimeReturnsPG(TimeReturnsRepo):
    def __init__(self):
        self.pgdb = PGConnection(
            host = "localhost",
            dbname = "equity",
            user = "postgres",
            password = "password",
            port = 5432
        )

    def infer_pg_type(self, dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "BIGINT"
        elif pd.api.types.is_float_dtype(dtype):
            return "DOUBLE PRECISION"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOLEAN"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return "TIMESTAMP"
        else:
            return "TEXT"

    def create_table(self, table: str, cols) -> None:
        columns = []
        for col in cols:
            col_type = self.infer_pg_type(col.dtype)
            columns.append(f'"{col}" {col_type}')

        cols_sql = ",\n    ".join(cols)

        return f"""
            CREATE TABLE IF NOT EXISTS {table} (
                {cols_sql}
            );
            """

    def read_csv(self, path: str, table: str, cols) -> None:
        conn, curr = self.pgdb.conn, self.pgdb.cursor

        create_sql = self.create_table(table, cols)
        curr.execute(create_sql)
        conn.commit()

        with open(path, "r") as f:
            with curr.copy(
                    f"COPY {table} FROM STDIN WITH CSV HEADER"
            ) as copy:
                copy.write(f.read())

        conn.commit()

    def read_df(self, data: DataFrame, table_name: str):
        engine = self.pgdb.getEngine()

        data.to_sql(
            table_name,
            con = engine,
            if_exists = "replace",
            index=False
        )

    def close_connection(self) -> None:
        self.pgdb.close()


