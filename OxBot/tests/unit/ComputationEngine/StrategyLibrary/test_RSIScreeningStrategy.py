
from unittest import TestCase
from OxBot.ComputationEngine.StrategyLibrary.RSIScreeningStrategyBuilder import RSIScreeningStrategyBuilder

from OxBot.ComputationEngine.StrategyLibrary.StrategyBuildingDirector import StrategyBuildingDirector

class TestRSIScreeningStrategy(TestCase):
  def test_can_build_rsi_screening_strategy(self):
    director = StrategyBuildingDirector()
    builder = RSIScreeningStrategyBuilder()
    director.builder = builder 
    director.buildLongStrategy()
    builder.strategy.listIndicators()
    self.assertEqual(True, builder.strategy.execute())
