from abc import abstractmethod, ABC

class Alphas(ABC):

    @abstractmethod
    def execute(self):
        pass