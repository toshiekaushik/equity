from ..models.DailyReturns import DailyReturns
import datetime

class DailyReturnsRepo():
    def add_returns(self, returns: DailyReturns):
        pass

    def get_returns(self, startDate: datetime, endDate: datetime, ticker: str) -> DailyReturns:
        pass

    def delete_stock_entries(self, startDate: datetime, endDate: datetime, ticker: str) -> None:
        pass

