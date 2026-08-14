from abc import abstractmethod, ABC

class StatTest(ABC):

    @abstractmethod
    def execute(self):
        pass