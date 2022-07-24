from alphabot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface
import pandas as pd
import pandas_ta as ta

class VolumeIndicator(IndicatorInterface):
    
  _days = 10
  _duration = 90
  _period = "1y"
  _results = pd.Series([],dtype=pd.StringDtype())
  
  def __init__(self, symbol: str, duration: int) -> None:
      self._symbol = symbol
      self._duration = duration

  def execute(self) -> bool:
      self.getAverageVolume()
      return True

  def isVolumeDesired(self, multiple: int) -> bool:
    return self.getAverageVolume(self._days) / self.getAverageVolume() > multiple 

  def getAverageVolume(self) -> pd.Series: 
    dataFrame = pd.DataFrame()
    data = dataFrame.ta.ticker(self._symbol, period = self._period)
    if data is not None:
      self._results = ta.sma(data["Volume"], self._duration)
    return self._results




