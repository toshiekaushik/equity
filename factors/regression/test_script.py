from CoreConsts import TECH_TICKERS
from factors.regression.Momentum_Weekly_Regression import Momentum_Weekly_Regression

regression = Momentum_Weekly_Regression(tickers = TECH_TICKERS)
regression.execute()