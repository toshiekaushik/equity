from data.collector.accumulators import Accumulate


class DailyReturns(Accumulate):
    def execute(self):
        print("DAILY RETURN")
