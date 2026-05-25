from data.collector.accumulators.DailyReturnsAcc import DailyReturnsAcc

acc = DailyReturnsAcc(tickers = ["aapl"])
acc.execute()