from pandas import Series, Timestamp
from alphabot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator
from alphabot.models import Symbol, Volume

class VolumeModel():
  _symbol = ""
  _duration = 0
  def __init__(self) -> None:
    self._tableName = 'alphabot_volume'

  def getVolumeData(self) -> Series:
    self._volumeIndicator = VolumeIndicator(self._symbol, self._duration)
    self._volumeIndicator.execute()
    return self._volumeIndicator._results

  def saveRecords(self, symbol: str, duration: int) -> bool:
    self._symbol = symbol
    self._duration = duration
    data = self.getVolumeData()
    if data is not None:
      for index, row in data.items():
        self.saveRecord(index, row)
    return True
  
  def saveRecord(self, priceDate: Timestamp, result: float) -> bool:
    symbolId = Symbol.objects.get(symbol = self._symbol).id
    volume = Volume(
      symbol_id = symbolId,
      date = priceDate.tz_localize('EST'),
      duration = self._duration,
      value = result,
    )
    volume.save()
    return True
