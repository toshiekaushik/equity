from Signal import Signals

class SignalStage:

    def __init__(self, config: list[dict]):
        self._signals = []

    @property
    def signals(self) -> list[Signals]:
        return self._signals

    @signals.setter
    def signals(self, config: list[dict]):
        self._signals = config
