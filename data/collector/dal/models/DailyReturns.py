from data.collector.dal.models import BaseModel
import datetime

class DailyReturns(BaseModel):
    def __init__(self, id,
                 date: datetime,
                 open: float,
                 high: float,
                 low: float,
                 close: float,
                 volume: int):
        super.__init__(id)
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume


