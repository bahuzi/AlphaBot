from abc import ABC, abstractmethod


class IndicatorInterface(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass    
