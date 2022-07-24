from unittest import TestCase
from alphabot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator

class TestRSIIndicator(TestCase):
  def test_get_indicator(self):
    indicator = RSIIndicator("AAPL", 9)
    self.assertTrue(indicator.execute())
  
  def test_none_type_symbol_can_escape(self):
    indicator = RSIIndicator("XXX", 5)
    self.assertTrue(indicator.execute())