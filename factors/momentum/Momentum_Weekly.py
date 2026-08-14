
from pandas.core.interchange.dataframe_protocol import DataFrame

from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors


class Momentum_Weekly(Factors):

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
        returns = self.calc(returns)
        print(returns.head())
        self.time_returns_pg.read_df(returns, "weekly_momentum_factor")
        self.time_returns_pg.close_connection()

    def calc(self, df: DataFrame):

        df = df.sort_values(['ticker', 'date'])

        df['mom_4_1'] = (
            df.groupby('ticker')['pct_change']
            .transform(lambda x: (1 + x.shift(1))
                       .rolling(4)
                       .apply(lambda r: r.prod() - 1, raw=True))
        )

        df['mom_12_1'] = (
            df.groupby('ticker')['pct_change']
            .transform(lambda x: (1 + x.shift(1))
                       .rolling(12)
                       .apply(lambda r: r.prod() - 1, raw=True))
        )

        df['mom_26_1'] = (
            df.groupby('ticker')['pct_change']
            .transform(lambda x: (1 + x.shift(1))
                       .rolling(26)
                       .apply(lambda r: r.prod() - 1, raw=True))
        )

        df['mom_52_1'] = (
            df.groupby('ticker')['pct_change']
            .transform(lambda x: (1 + x.shift(1))
                       .rolling(52)
                       .apply(lambda r: r.prod() - 1, raw=True))
        )
        df.dropna(inplace = True)
        return df

    def create_query(self) -> str:
        ticker_str = ",".join(["'" + ticker + "'" for ticker in self.tickers])
        return f"""
        SELECT *
        FROM weekly_returns
        WHERE ticker IN ({ticker_str})
        """

