import datetime
from data.collector.dal.models.Stock import Stock

class WeeklyReturns(Stock):
    def __init__(self, ticker: str,
                 date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: int):
        super().__init__(ticker)
        self._date = date
        self._open = open
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def open(self) -> float:
        return self._open

    @property
    def high(self) -> float:
        return self._high

    @property
    def low(self) -> float:
        return self._low

    @property
    def close(self) -> float:
        return self._close

    @property
    def volume(self) -> int:
        return self._volume
