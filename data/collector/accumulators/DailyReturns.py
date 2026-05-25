from pandas.io.sas.sas_constants import dataset_offset

from data.collector.accumulators import Accumulate
from data.collector.clients.tiingo.api.fundamentals import DailyData as dd
from data.collector.clients.tiingo.api.endpoints import TiingoEndpoints
import pandas as pd
import os

from data.collector.dal.db.postgress.DailyReturnsPG import DailyReturnsPG

TIINGO_TOKEN = "a2b70640dcb7265f5bc4c7653f52f4c9a6516b6f"
HEADERS = {
    'Content-Type': 'application/json'
}

class DailyReturns(Accumulate):

    def __init__(self, tickers: list[str]):
        self.tickers = tickers

    def execute(self) -> None:
        for ticker in self.tickers:
            daily_returns_req = self.buildRequest(ticker)
            resp = daily_returns_req.getResponse()
            df = pd.read_csv(resp)
            df.to_csv("/Users/parit/market-models/equity/data/daily_returns.csv", index = False)
            DailyReturnsPG.read_csv("/Users/parit/market-models/equity/data/daily_returns.csv")
            os.remove("/Users/parit/market-models/equity/data/daily_returns.csv")

    def buildRequest(self, ticker: str) -> dd:
        daily_returns = dd(TiingoEndpoints.DAILY_FUNDAMENTAL, HEADERS, {})
        daily_returns.setTicker(ticker)
        daily_returns.setFormat("csv")
        daily_returns.setToken(TIINGO_TOKEN)
        daily_returns.setStartDate("2026-01-01")
        return daily_returns



