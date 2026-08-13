from factors.momentum.Momentum_Monthly import Momentum_Monthly
from factors.momentum.Momentum_Weekly import Momentum_Weekly

# signals = Momentum_Monthly(tickers = ["MSFT", "AMZN", "GOOG", "AAPL"])
signals = Momentum_Weekly(tickers = ["MSFT", "AMZN", "GOOG", "AAPL"])
signals.execute()