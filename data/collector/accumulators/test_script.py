from data.collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.time_returns.MonthlyReturnsAcc import MonthlyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

acc = MonthlyReturnsAcc(tickers = ["MSFT", "AMZN", "GOOG", "AAPL", "NFLX"])

acc.execute()