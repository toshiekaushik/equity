from data.collector.accumulators.time_returns.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.time_returns.WeeklyReturnsAcc import WeeklyReturnsAcc

CLASS_REGISTRY = {
    "DAILY_RETURNS": DailyReturnsAcc,
    "WEEKLY_RETURNS": WeeklyReturnsAcc
}
