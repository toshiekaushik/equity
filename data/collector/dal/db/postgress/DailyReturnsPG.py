import os

import pandas as pd

from data.collector.dal.db.postgress.PGConnection import PGConnection
from data.collector.dal.interfaces.DailyReturnsRepo import DailyReturnsRepo
from data.collector.dal.models.DailyReturns import DailyReturns


class DailyReturnsPG(DailyReturnsRepo):
    def __init__(self):
        self.pgdb = PGConnection(
            host = "localhost",
            dbname = "equity",
            user = "name@example.com",
            password = "password",
            port = 5432
        )

    def read_csv(self, path: str):
        conn, curr = self.pgdb.conn, self.pgdb.cursor

        with open(path, 'r') as f:
            next(f)
            curr.copy(f, 'daily_returns', sep = ',')

        conn.commit()



