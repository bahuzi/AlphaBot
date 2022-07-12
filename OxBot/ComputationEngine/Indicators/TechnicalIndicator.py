from typing import List
from OxBot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface


class TechnicalIndicator(IndicatorInterface):
    
    def __init__(self) -> None:
        self._children: List[IndicatorInterface] = []
        self._type: str = "technical"

    def execute(self) -> bool:
        results = []
        for child in self._children:
            results.append(child.execute())
        print("Shoulde return: ", results)
        return results
    
    def add(self, indicator: IndicatorInterface) -> None:
        self._children.append(indicator)

    def remove(self, indicator: IndicatorInterface) -> None:
        self._children.remove(indicator)

    def is_composite(self) -> bool:
        return True

