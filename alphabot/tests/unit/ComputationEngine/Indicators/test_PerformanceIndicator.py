from unittest import TestCase
from alphabot.ComputationEngine.Indicators.PerformanceIndicator import PerformanceIndicator

class TestPerformanceIndicator(TestCase):
  def test_performance_indicator(self):
    indicator = PerformanceIndicator("AAPL", 50)
    self.assertTrue(indicator.execute())

  def test_none_type_symbol_can_escape(self):
    indicator = PerformanceIndicator("XXX", 100)
    self.assertTrue(indicator.execute())