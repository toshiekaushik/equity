from data.collector.accumulators.DailyReturnsAcc import DailyReturnsAcc
from data.collector.accumulators.WeeklyReturnsAcc import WeeklyReturnsAcc

CLASS_REGISTRY = {
    "DAILY_RETURNS": DailyReturnsAcc,
    "WEEKLY_RETURNS": WeeklyReturnsAcc
}
