from Alphas import Alphas

class AlphaStage:
    def __init__(self, config: list[dict]):
        self._strategies = []

    @property
    def strategies(self) -> list[Alphas]:
        return self._strategies

    @strategies.setter
    def strategies(self, config: list[dict]):
        self._strategies = config
