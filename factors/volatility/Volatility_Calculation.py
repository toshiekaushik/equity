from pydantic_core.core_schema import TimeSchema

from data.collector.dal.db.postgress.FactorPG import FactorPG
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors


class Volatility_Calculation(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = params
        self.time_returns = TimeReturnsPG()
        # self.factor_pg = FactorPG()

    def execute(self) -> None:
        returns = self.time_returns.get_daily_returns("2022-01-01", "2026-08-17", self.tickers)
        returns["pct_change"] = (
            returns["close"].pct_change()
        )
        returns = returns.sort_values(['ticker', 'date'])
        vol = returns[["ticker", "date", "pct_change"]]
        vol['volatility'] = (
            vol.groupby('ticker')['pct_change']
            .transform(lambda x: x.shift(1).rolling(20).std())
        )
        vol.dropna(inplace = True)
        print("Volatility Head:\n", vol.head())
        self.time_returns.read_df(vol, "volatility_20_days")


