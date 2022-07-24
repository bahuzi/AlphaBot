from unittest import TestCase
from alphabot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator
from alphabot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator
from alphabot.ComputationEngine.Indicators.TechnicalIndicator import TechnicalIndicator
from alphabot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator

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
    