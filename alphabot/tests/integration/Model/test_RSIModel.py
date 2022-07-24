import os
from django.test import TestCase
from alphabot.Model.RSIModel import RSIModel
from alphabot.Model.SymbolModel import SymbolModel

class TestRSIModel(TestCase):
  def test_save_json_records(self):
    symbol = SymbolModel()
    path = os.path.dirname(os.path.relpath(__file__))
    data = symbol.readJson("amex_sample_tickers.json", path)
    symbol.saveRecords(data)
    model = RSIModel()
    self.assertEqual(True, model.saveRecords("GS", 9))