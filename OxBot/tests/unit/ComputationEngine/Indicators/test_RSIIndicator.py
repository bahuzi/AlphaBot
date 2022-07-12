from unittest import TestCase

from OxBot.ComputationEngine.Indicators.RSIIndicator import RSIIndicator


class TestRSIIndicator(TestCase):
  def testGetIndicator(self):
    indicator = RSIIndicator("AAPL", 9)
    self.assertTrue(indicator.execute())
    self.assertTrue(indicator.isRSIDesired(9))
    self.assertEqual(27, indicator.getRSI(9))