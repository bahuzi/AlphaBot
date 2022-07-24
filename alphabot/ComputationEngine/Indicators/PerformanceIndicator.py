from alphabot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface
import pandas as pd
import pandas_ta as ta

class PerformanceIndicator(IndicatorInterface):
    
    _desiredDelta = 0.2
    _duration = 50
    _period = "1y"
    _results = pd.Series([],dtype=pd.StringDtype())

    def __init__(self, symbol: str, duration: int = 50) -> None:
        self._symbol = symbol
        self._duration = duration

    def execute(self) -> bool:
        self.getPerformance()
        return True

    def isPerformanceDesired(self) -> bool:
      delta = self.getDelta()
      if self._delta is None:
        return delta < 0 and abs(delta) > self._desiredDelta

      return delta < 0 and abs(delta) > self._delta

    def getPerformance(self) -> pd.Series: 
      dataFrame = pd.DataFrame()
      data = dataFrame.ta.ticker(self._symbol, period = self._period)
      if data is not None:
        self._results = ta.sma(data["Close"], self._duration)
      return self._results




