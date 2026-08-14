from abc import ABC, abstractmethod

from factors.stat_tests.StatTest import StatTest

class Correlation(StatTest):

    @abstractmethod
    def execute(self):
        pass