from unittest import TestCase
from OxBot.ComputationEngine.Indicators.CashBurnIndicator import CashBurnIndicator
from OxBot.ComputationEngine.Indicators.FinancialIndicator import FinancialIndicator

class TestFinancialIndicator(TestCase):
  def test_financial_indicator(self):
    indicator = FinancialIndicator()
    cashBurnIndicator = CashBurnIndicator("AAPL", 2)
    indicator.add(cashBurnIndicator)
    indicator.remove(cashBurnIndicator)
    self.assertEqual("financial", indicator._type)
    self.assertEqual([], indicator.execute())
    