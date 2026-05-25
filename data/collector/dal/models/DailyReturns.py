from data.collector.dal.models.Stock import Stock
import datetime

class DailyReturns(Stock):
    def __init__(self, ticker: str,
                 date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: int):
        super().__init__(ticker)
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    @property
    def ticker(self) -> str:
        return self.ticker

    @property
    def date(self) -> datetime:
        return self.date

    @property
    def open(self) -> float:
        return self.open

    @property
    def high(self) -> float:
        return self.high

    @property
    def low(self) -> float:
        return self.low

    @property
    def close(self) -> float:
        return self.close

    @property
    def volumne(self) -> int:
        return self.volume
