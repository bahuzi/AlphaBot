from typing import List
from alphabot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface


class FinancialIndicator(IndicatorInterface):
    
    def __init__(self) -> None:
        self._children: List[IndicatorInterface] = []
        self._type: str = "financial"

    def execute(self) -> bool:
        results = []
        for child in self._children:
            results.append(child.execute())
        print("should return: ", results)
        return results
    
    def add(self, indicator: IndicatorInterface) -> None:
        self._children.append(indicator)

    def remove(self, indicator: IndicatorInterface) -> None:
        self._children.remove(indicator)

    def is_composite(self) -> bool:
        return True

