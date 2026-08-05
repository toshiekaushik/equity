from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from signals.Signal import Signals


class Momentum_Monthly(Signals):

    def __init__(self, tickers: list[str]):
        self.tickers = tickers
        self.time_returns_pg = TimeReturnsPG()

    def execute(self) -> None:
        query = self.create_query()
        df = self.time_returns_pg.execute_query(query)
        print("Monthly Returns DataFrame Head:\n", df.head())
        df["pct_change"] = (
            df.groupby("ticker")["close"].pct_change()
        )
        returns = df[["date", "ticker", "pct_change"]]
        self.time_returns_pg.read_df(returns, "monthly_momentum")
        self.time_returns_pg.close_connection()

    def create_query(self) -> str:
        ticker_str = ",".join(["'" + ticker + "'" for ticker in self.tickers])
        return f"""
        SELECT *
        FROM monthly_returns 
        WHERE ticker IN ({ticker_str})
        """

