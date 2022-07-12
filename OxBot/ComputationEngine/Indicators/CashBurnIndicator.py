from OxBot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface

class CashBurnIndicator(IndicatorInterface):

    _duration = 2

    def __init__(self, symbol: str, duration: float = None) -> None:
        self._symbol = symbol
        self._duration = duration

    def execute(self) -> bool:
        self.isCashDesired()
        print("CashBurnIndicator is triggered and is fine")
        return True

    def isCashDesired(self) -> bool:
      cashHolding = self.getCashHolding()
      projectedNetIncome = self.getProjectedNetIncome(self._duration)
      return cashHolding > projectedNetIncome

    def getCashHolding(self) -> float:
      return 100 # TODO: add code for rolling number of days 

    def getProjectedNetIncome(self, duration: float = None) -> float:
      return 99 # TODO: add code for rolling number of days 




