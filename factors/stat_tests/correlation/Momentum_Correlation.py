from factors.stat_tests.correlation.Correlation import Correlation


class Momentum_Correlation(Correlation):

    def __init__(self, tickers: list[str], params = None):
        self.tickers = tickers
        self.params = None

    def execute(self) -> None:
        pass


