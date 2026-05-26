from data.collector.accumulators.DailyReturnsAcc import DailyReturnsAcc

acc = DailyReturnsAcc(tickers = ["AAPL", "GOOG", "AMZN"])

acc.execute()