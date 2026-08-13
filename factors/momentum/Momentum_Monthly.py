from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors


class Momentum_Monthly(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = None
        self.time_returns_pg = TimeReturnsPG()

    def execute(self) -> None:
        query = self.create_query()
        df = self.time_returns_pg.execute_query(query)
        print("Monthly Returns DataFrame Head:\n", df.head())
        df["pct_change"] = (
            df.groupby("ticker")["close"].pct_change()
        )
        returns = df[["date", "ticker", "pct_change"]]
        returns.dropna(subset = ["pct_change"], inplace = True)
        self.time_returns_pg.read_df(returns, "monthly_momentum_factor")
        self.time_returns_pg.close_connection()

    # def calc_

    def create_query(self) -> str:
        ticker_str = ",".join(["'" + ticker + "'" for ticker in self.tickers])
        return f"""
        SELECT *
        FROM monthly_returns 
        WHERE ticker IN ({ticker_str})
        """

