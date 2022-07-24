import os
from django.test import TestCase
from alphabot.Model.VolumeModel import VolumeModel
from alphabot.Model.SymbolModel import SymbolModel
from alphabot.models import Symbol, Volume

class TestVolumeModel(TestCase):
  def test_save_volume_records(self):
    symbol = SymbolModel()
    path = os.path.dirname(os.path.relpath(__file__))
    data = symbol.readJson("amex_sample_tickers.json", path)
    symbol.saveRecords(data)
    symbolObject = Symbol.objects.get(symbol = "GS")
    model = VolumeModel()
    model.saveRecords("GS", 90)
    self.assertEqual(symbolObject.id, Volume.objects.filter(duration = 90)[0].symbol_id)