from pandas import Series, Timestamp
from alphabot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator
from alphabot.models import Symbol, Performance

class PerformanceModel():
  _symbol = ""
  _duration = 0
  def __init__(self) -> None:
    self._tableName = 'alphabot_performance'

  def getPerformanceData(self) -> Series:
    self._performanceIndicator = PerformanceIndicator(self._symbol, self._duration)
    self._performanceIndicator.execute()
    return self._performanceIndicator._results

  def saveRecords(self, symbol: str, duration: int) -> bool:
    self._symbol = symbol
    self._duration = duration
    data = self.getPerformanceData()
    if data is not None:
      for index, row in data.items():
        self.saveRecord(index, row)
    return True
  
  def saveRecord(self, priceDate: Timestamp, result: float) -> bool:
    symbolId = Symbol.objects.get(symbol = self._symbol).id
    performance = Performance(
      symbol_id = symbolId,
      date = priceDate.tz_localize('EST'),
      duration = self._duration,
      value = result,
    )
    performance.save()
    return True
