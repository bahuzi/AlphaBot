from OxBot.ComputationEngine.Indicators.IndicatorInterface import IndicatorInterface

class RSIScreeningStrategy():
  def __init__(self) -> None:
    self.indicators = []

  def add(self, indicator: IndicatorInterface) -> None:
    self.indicators.append(indicator)

  def listIndicators(self) -> None:
    print("List all indicators: ", self.indicators)

  def execute(self) -> bool:
    for indicator in self.indicators:
      indicator.execute()
    print("Strategy is successfully executed!")
    return True
