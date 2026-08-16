import math

from pandas import DataFrame

from data.collector.dal.db.postgress.FactorPG import FactorPG
from data.collector.dal.db.postgress.TimeReturnsPG import TimeReturnsPG
from factors.Factor import Factors

import numpy as np
import statsmodels.api as sm

class Momentum_Weekly_Regression(Factors):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = params
        self.time_returns_pg = TimeReturnsPG()
        self.factor_pg = FactorPG()

    def execute(self):
        momentum = self.factor_pg.get_momentum_weekly("2023-01-01", "2026-08-01", self.tickers)
        returns = self.time_returns_pg.get_returns("2023-01-01", "2026-08-01", self.tickers)
        print("Momentum DataFrame Head:\n", momentum.head())
        returns["pct_change"] = (
            returns.groupby("ticker")["close"].pct_change()
        )
        returns.dropna(inplace = True)
        print("Returns DataFrame Head:\n", returns.head())

        momentum = momentum.sort_values(["ticker", "date"])
        returns = returns.sort_values(["ticker", "date"])

        df = momentum.merge(
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
        mom_4_1_returns = []
        mom_12_1_returns = []
        for date, cross_section in data.groupby("date"):
            mom_4_1_coef, mom_12_1_coeff = self.regression(cross_section)
            mom_4_1_returns.append(mom_4_1_coef)
            mom_12_1_returns.append(mom_12_1_coeff)
        # print("These are the first 10 factor returns: ", factor_returns[:10])
        mom_4_1_returns = [val for val in mom_4_1_returns if not math.isnan(val)]
        mom_12_1_returns = [val for val in mom_12_1_returns if not math.isnan(val)]
        print("Average factor 4 weeks return: ", np.nansum(mom_4_1_returns) / len(mom_4_1_returns))
        print("Average factor 12 weeks return: ", np.nansum(mom_12_1_returns) / len(mom_12_1_returns))


    def regression(self, cross_section: DataFrame) -> tuple:
        X = cross_section[["mom_4_1", "mom_12_1"]]
        Y = cross_section["next_week_return"]

        X = sm.add_constant(X)

        model = sm.OLS(Y, X).fit()

        return (model.params["mom_4_1"], model.params["mom_12_1"])



