from unittest import TestCase
from OxBot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator

class TestVolumeIndicator(TestCase):
  def testGetIndicator(self):
    indicator = VolumeIndicator("AAPL", 3)
    self.assertTrue(indicator.execute())
    self.assertEqual(True, indicator.isVolumeDesired(3))