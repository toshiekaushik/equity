import math

from pandas import DataFrame

from data.collector.dal.db.postgress.FactorPG import FactorPG
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors

import numpy as np
import statsmodels.api as sm

class Reversal_Weekly_Regression(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = params
        self.time_returns_pg = TimeReturnsPG()
        self.factor_pg = FactorPG()

    def execute(self):
        reversal = self.factor_pg.get_reversal_weekly("2023-01-01", "2026-08-01", self.tickers)
        returns = self.time_returns_pg.get_returns("2023-01-01", "2026-08-01", self.tickers)
        print("Reversal DataFrame Head:\n", reversal.head())
        returns["pct_change"] = (
            returns.groupby("ticker")["close"].pct_change()
        )
        returns.dropna(inplace = True)
        print("Returns DataFrame Head:\n", returns.head())

        reversal = reversal.sort_values(["ticker", "date"])
        returns = returns.sort_values(["ticker", "date"])

        df = reversal.merge(
            returns[["ticker", "date", "pct_change"]],
            on=["ticker", "date"],
            how="inner"
        )

        df["next_week_return"] = (
            df.groupby("ticker")["pct_change"].shift(-1)
        )

        print("Combined and Shifted dataframe:\n", df.head())

        self.cross_sectional_regression(df)

    def cross_sectional_regression(self, data: DataFrame):
        factor_returns = []
        for date, cross_section in data.groupby("date"):
            ret = self.regression(cross_section)
            factor_returns.append(ret)
        # print("These are the first 10 factor returns: ", factor_returns[:10])
        factor_returns = [val for val in factor_returns if not math.isnan(val)]
        print("Average reversal factor return: ", np.nansum(factor_returns) / len(factor_returns))

    def regression(self, cross_section: DataFrame) -> tuple:
        X = cross_section["reversal_chg"]
        Y = cross_section["next_week_return"]

        X = sm.add_constant(X)

        model = sm.OLS(Y, X).fit()

        return model.params["reversal_chg"]



