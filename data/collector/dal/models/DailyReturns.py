from data.collector.dal.models import Stock
import datetime

class DailyReturns(Stock):
    def __init__(self, ticker: str,
                 date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: int):
        super.__init__(ticker,
                       date,
                       open,
                       high,
                       low,
                       close,
                       volume)



