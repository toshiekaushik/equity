from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

acc = WeeklyReturnsAcc(tickers = ["AAPL", "GOOG", "AMZN", "TSLA"])

acc.execute()