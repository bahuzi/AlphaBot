from unittest import TestCase
from OxBot.ComputationEngine.Indicators.CashBurnIndicator import CashBurnIndicator

class TestCashBurnIndicator(TestCase):
  def test_cash_burn_indicator(self):
    indicator = CashBurnIndicator("AAPL", 2)
    self.assertTrue(indicator.execute())
    self.assertEqual(True, indicator.isCashDesired())