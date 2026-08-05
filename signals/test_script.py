from signals.momentum.Momentum_Monthly import Momentum_Monthly

signals = Momentum_Monthly(tickers = ["MSFT", "AMZN", "GOOG", "AAPL"])

signals.execute()