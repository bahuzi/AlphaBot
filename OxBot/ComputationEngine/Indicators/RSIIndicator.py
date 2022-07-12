from OxBot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface


class RSIIndicator(IndicatorInterface):
    
    _desiredRSI = 30
    
    def __init__(self, symbol: str, days: int) -> None:
        self._symbol = symbol
        self._days = days

    def execute(self) -> bool:
        self.getRSI(self._days)
        print("RSIIndicator is triggered and is fine")
        return True

    def isRSIDesired(self, days: int) -> bool:
      return self.getRSI(days) < self._desiredRSI

    def getRSI(self, days: int) -> float:
      print("run the calculation")
      return 3 * days # TODO: add code


