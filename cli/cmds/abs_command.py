from abc import ABC, abstractmethod


class AbsCommand(ABC):

    @abstractmethod
    def execute(self):
        pass
