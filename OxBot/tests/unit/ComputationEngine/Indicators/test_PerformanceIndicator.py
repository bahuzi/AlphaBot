from unittest import TestCase
from OxBot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator

class TestPerformanceIndicator(TestCase):
  def test_performance_indicator(self):
    indicator = PerformanceIndicator("AAPL", 0.2)
    self.assertTrue(indicator.execute())
    self.assertEqual(True, indicator.isPerformanceDesired())