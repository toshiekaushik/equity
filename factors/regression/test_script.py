from CoreConsts import TECH_TICKERS
from factors.regression.Cross_Sectional_Regression import Cross_Sectional_Regression
from factors.regression.Momentum_Weekly_Regression import Momentum_Weekly_Regression
from factors.regression.Reversal_Weekly_Regression import Reversal_Weekly_Regression

# regression = Momentum_Weekly_Regression(tickers = TECH_TICKERS)
# regression = Reversal_Weekly_Regression(tickers = TECH_TICKERS)
regression = Cross_Sectional_Regression(tickers = TECH_TICKERS)
regression.execute()