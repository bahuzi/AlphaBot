from OxBot.ComputationEngine.Indicators.IndicatorInterface import \
    IndicatorInterface

class VolumeIndicator(IndicatorInterface):
    
    _days = 10
    
    def __init__(self, symbol: str, multiple: int) -> None:
        self._symbol = symbol
        self._multiple = multiple

    def execute(self) -> bool:
        self.isVolumeDesired(self._multiple)
        print("VolumeIndicator is triggered and is fine")
        return True

    def isVolumeDesired(self, multiple: int) -> bool:
      print("run the calculation")
      return self.getAverageVolume(self._days) / self.getAverageVolume() > multiple 

    def getAverageVolume(self, days: int = None) -> float: 
      valume = days # TODO: add code
      if valume is None:
        return 3
      return valume




