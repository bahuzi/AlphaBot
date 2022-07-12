from OxBot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface

class PerformanceIndicator(IndicatorInterface):
    
    _desiredDelta = 0.2
    _duration = 60

    def __init__(self, symbol: str, delta: float = None) -> None:
        self._symbol = symbol
        self._delta = delta

    def execute(self) -> bool:
        self.isPerformanceDesired()
        print("PerformanceIndicator is triggered and is fine")
        return True

    def isPerformanceDesired(self) -> bool:
      delta = self.getDelta()
      if self._delta is None:
        return delta < 0 and abs(delta) > self._desiredDelta

      return delta < 0 and abs(delta) > self._delta

    def getDelta(self, duration: int = None) -> float: 
      if duration is None:
        return -0.4 # TODO: add code for ytd lowest point 
      return -0.3 # TODO: add code for rolling number of days 




