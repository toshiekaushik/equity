from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors

class Reversal_Weekly(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = params
        self.time_returns_pg = TimeReturnsPG()

    def execute(self) -> None:
        returns = self.time_returns_pg.get_returns(
            "2014-01-01",
            "2026-08-17",
            self.tickers
        )
        print("Weekly Returns HEAD:\n", returns.head())
        returns["pct_change"] = (
            returns.groupby("ticker")["close"].pct_change()
        )
        returns.dropna(inplace = True)
        returns["reversal_chg"] = -returns["pct_change"]
        self.time_returns_pg.read_df(returns, "weekly_reversal_factor")
        self.time_returns_pg.close_connection()


