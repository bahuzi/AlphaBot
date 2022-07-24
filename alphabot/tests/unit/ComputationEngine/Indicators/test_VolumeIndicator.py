from unittest import TestCase
from alphabot.ComputationEngine.Indicators.VolumeIndicator import VolumeIndicator

class TestVolumeIndicator(TestCase):
  def testGetIndicator(self):
    indicator = VolumeIndicator("AAPL", 90)
    self.assertTrue(indicator.execute())
  
  def test_none_type_symbol_can_escape(self):
    indicator = VolumeIndicator("XXX", 50)
    self.assertTrue(indicator.execute())