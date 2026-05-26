import datetime

class TimeReturns:
    def __init__(self, date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close

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