from CoreConsts import TECH_TICKERS
from factors.reversal.Reversal_Weekly import Reversal_Weekly

reversal_factor = Reversal_Weekly(TECH_TICKERS)
reversal_factor.execute()