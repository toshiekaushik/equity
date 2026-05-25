from typing import Any

import psycopg
from psycopg import Connection, Cursor


class PGConnection:
    def __init__(self, host: str,
                 dbname: str,
                 user: str,
                 password: str,
                 port: int):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.conn = self.create_conn()
        self.cursor = self.conn.cursor()

    def create_conn(self) -> Connection:
        return psycopg.connect(
            host = self.host,
            dbname = self.dbname,
            user = self.user,
            password = self.password,
            port = self.port
        )

    @property
    def conn(self) -> Connection:
        return self.conn

    @property
    def cursor(self) -> Cursor[Any]:
        return self.cursor
