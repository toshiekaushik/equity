from CoreConsts import TECH_TICKERS
from factors.momentum.Momentum_Weekly import Momentum_Weekly

# signals = Momentum_Monthly(tickers = ["MSFT", "AMZN", "GOOG", "AAPL"])
signals = Momentum_Weekly(tickers = TECH_TICKERS)
signals.execute()