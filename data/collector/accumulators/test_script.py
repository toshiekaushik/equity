from data.collector.accumulators.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.WeeklyReturnsAcc import WeeklyReturnsAcc

acc = WeeklyReturnsAcc(tickers = ["AAPL", "GOOG", "AMZN"])

acc.execute()