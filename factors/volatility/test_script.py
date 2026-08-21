from CoreConsts import TECH_TICKERS
from factors.volatility.Volatility_Calculation import Volatility_Calculation

vol = Volatility_Calculation(TECH_TICKERS)
vol.execute()
