from alphabot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface
import pandas as pd
import pandas_ta as ta

class RSIIndicator(IndicatorInterface):
    
    _desiredRSI = 30
    _duration = 9
    _period = "1y"
    _results = pd.Series([],dtype=pd.StringDtype())
    
    def __init__(self, symbol: str, duration: int) -> None:
        self._symbol = symbol
        self._duration = duration

    def execute(self) -> bool:
        self.getRSI()
        return True

    def isRSIDesired(self, days: int) -> bool:
      return self.getRSI(days) < self._desiredRSI

    def getRSI(self) -> pd.Series:
        dataFrame = pd.DataFrame()
        data = dataFrame.ta.ticker(self._symbol, period = self._period)
        if data is not None:
            self._results = ta.rsi(data["Close"], self._duration)
        return self._results


