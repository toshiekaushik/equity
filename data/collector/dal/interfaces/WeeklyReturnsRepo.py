from pandas import DataFrame

from ..models.WeeklyReturns import WeeklyReturns
import datetime

class WeeklyReturnsRepo():
    def add_returns(self, returns: WeeklyReturns):
        pass

    def get_returns(self, startDate: datetime, endDate: datetime, ticker: str) -> WeeklyReturns:
        pass

    def delete_stock_entries(self, startDate: datetime, endDate: datetime, ticker: str) -> None:
        pass

    def read_csv(self, path: str, table: str, cols):
        pass

    def read_df(self, df: DataFrame, table_name: str):
        pass