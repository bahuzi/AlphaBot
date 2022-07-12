

from OxBot.ComputationEngine.StrategyLibrary.RSIScreeningStrategyBuilder import RSIScreeningStrategyBuilder


class StrategyBuildingDirector:

  def __init__(self) -> None:
    self._buider = None

  @property
  def builder(self) -> RSIScreeningStrategyBuilder:
      return self._builder

  @builder.setter
  def builder(self, builder: RSIScreeningStrategyBuilder) -> None:
      self._builder = builder

  def buildLongStrategy(self) -> None:
    self.builder.setTechnicalIndicators()
    self.builder.setFinancialIndicators()