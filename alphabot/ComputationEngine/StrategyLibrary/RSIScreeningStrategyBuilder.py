
from alphabot.ComputationEngine.Indicators.CashBurnIndicator import CashBurnIndicator
from alphabot.ComputationEngine.Indicators.FinancialIndicator import FinancialIndicator
from alphabot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator
from alphabot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator
from alphabot.ComputationEngine.Indicators.TechnicalIndicator import TechnicalIndicator
from alphabot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator
from alphabot.ComputationEngine.StrategyLibrary.RSIScreeningStrategy import RSIScreeningStrategy
from alphabot.ComputationEngine.StrategyLibrary.StrategyBuilderInterface import StrategyBuilderInterface


class RSIScreeningStrategyBuilder(StrategyBuilderInterface):
  def __init__(self) -> None:
    self.reset()

  def reset(self) -> None:
    self._strategy = RSIScreeningStrategy()

  @property
  def strategy(self) -> RSIScreeningStrategy:
    strategy = self._strategy
    self.reset()
    return strategy

  def setTechnicalIndicators(self) -> None:
    indicator = TechnicalIndicator()
    indicator.add(RSIIndicator("AAPL", 9))
    indicator.add(VolumeIndicator("AAPL", 3))
    indicator.add(PerformanceIndicator("AAPL", 0.2))
    self._strategy.add(indicator)
  
  def setFinancialIndicators(self) -> None:
    indicator = FinancialIndicator()
    indicator.add(CashBurnIndicator("AAPL", 2))
    self._strategy.add(indicator)

  

