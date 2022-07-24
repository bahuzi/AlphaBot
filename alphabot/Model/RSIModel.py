from pandas import Series, Timestamp
from alphabot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator
from alphabot.models import RSI, Symbol

class RSIModel():
  _symbol = ""
  _duration = 0
  def __init__(self) -> None:
    self._tableName = 'alphabot_rsi'

  def getRSIData(self) -> Series:
    self._risIndicator = RSIIndicator(self._symbol, self._duration)
    self._risIndicator.execute()
    return self._risIndicator._results

  def saveRecords(self, symbol: str, duration: int) -> bool:
    self._symbol = symbol
    self._duration = duration
    data = self.getRSIData()
    if data is not None:
      for index, row in data.items():
        self.saveRecord(index, row)
    return True
  
  def saveRecord(self, priceDate: Timestamp, result: float) -> bool:
    symbolId = Symbol.objects.get(symbol = self._symbol).id
    rsi = RSI(
      symbol_id = symbolId,
      date = priceDate.tz_localize('EST'),
      duration = self._duration,
      value = result,
    )
    rsi.save()
    return True
