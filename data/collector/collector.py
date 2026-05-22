from response import Response

from data.clients.tiingo.api.tiingoClient import TiingoClient

class CollectorStage:
    def __init__(self, tickers: list[str], dependents: list[str]):
        self.tickers = tickers
        self.dependents = dependents
        self.tiingoClient = TiingoClient()

