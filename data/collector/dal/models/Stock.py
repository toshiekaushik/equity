import datetime

class Stock:
    def __init__(self, ticker: str,
                 date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: int):
        super.__init__(ticker)
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume