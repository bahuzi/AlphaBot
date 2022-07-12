from unittest import TestCase
from OxBot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator
from OxBot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator
from OxBot.ComputationEngine.Indicators.TechnicalIndicator import TechnicalIndicator
from OxBot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator

class TestTechnicalIndicator(TestCase):
  def test_technical_indicator(self):
    indicator = TechnicalIndicator()
    rsiIndicator = RSIIndicator("AAPL", 9)
    indicator.add(rsiIndicator)
    indicator.add(VolumeIndicator("AAPL", 3))
    indicator.add(PerformanceIndicator("AAPL", 0.2))
    indicator.remove(rsiIndicator)
    self.assertEqual("technical", indicator._type)
    self.assertEqual([True, True], indicator.execute())
    