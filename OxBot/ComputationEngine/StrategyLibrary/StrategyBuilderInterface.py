from abc import ABC, abstractmethod


class StrategyBuilderInterface(ABC):
    
    @property
    @abstractmethod
    def strategy(self) -> None:
        pass

    @abstractmethod
    def setTechnicalIndicators(self) -> None:
        pass  

    @abstractmethod
    def setFinancialIndicators(self) -> None:
        pass  
