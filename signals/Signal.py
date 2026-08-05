from abc import abstractmethod, ABC

class Signals(ABC):

    @abstractmethod
    def execute(self):
        pass