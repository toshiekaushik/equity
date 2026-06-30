
class AlphaStage:
    def __init__(self, config: list[dict]):
        self._strategies = []

    @property
    def strategies(self) -> list:
        return self._strategies

    @strategies.setter
    def strategies(self, config: list[dict]):
        self._strategies = config
