from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors


class Reversal_Weekly(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = params
        self.time_returns_pg = TimeReturnsPG()

    def execute(self) -> None:


