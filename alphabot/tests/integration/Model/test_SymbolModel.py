from django.test import TestCase
from alphabot.Model.SymbolModel import SymbolModel
import os

class TestSymbolModel(TestCase):
  def test_save_json_records(self):
    symbol = SymbolModel()
    path = os.path.dirname(os.path.relpath(__file__))
    data = symbol.readJson("amex_sample_tickers.json", path)
    symbol.saveRecords(data)
    self.assertEqual(True, symbol.saveRecords(data))