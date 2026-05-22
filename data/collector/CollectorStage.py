from data.collector.accumulators import Accumulate


class CollectorStage:
    def __init__(self, tickers: list[str], accumulators: list[Accumulate]):
        self._tickers = tickers
        self._accumulators = accumulators

    @property
    def accumulators(self) -> list[Accumulate]:
        return self._accumulators

    @property
    def tickers(self) -> list[str]:
        return self._tickers

    @tickers.setter
    def tickers(self, tickers: list[str]) -> None:
        self._tickers = tickers

    @accumulators.setter
    def accumulators(self, accumulators: list[Accumulate]) -> None:
        self._accumulators = accumulators

    def execute(self) -> None:
        for acc in self._accumulators:
            acc.execute()



