from abc import abstractmethod, ABC

class Factors(ABC):

    @abstractmethod
    def execute(self):
        pass