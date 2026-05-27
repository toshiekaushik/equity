from data.collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

acc = MonthlyReturnsAcc(tickers = ["AAPL", "GOOG", "AMZN", "TSLA"])

acc.execute()