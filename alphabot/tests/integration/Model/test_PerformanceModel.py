import os
from django.test import TestCase
from alphabot.Model.PerformanceModel import PerformanceModel
from alphabot.Model.SymbolModel import SymbolModel
from alphabot.models import Symbol, Performance

class TestPerformanceModel(TestCase):
  def test_save_json_records(self):
    symbol = SymbolModel()
    path = os.path.dirname(os.path.relpath(__file__))
    data = symbol.readJson("amex_sample_tickers.json", path)
    symbol.saveRecords(data)
    symbolObject = Symbol.objects.get(symbol = "GS")
    model = PerformanceModel()
    model.saveRecords("GS", 50)
    self.assertEqual(symbolObject.id, Performance.objects.filter(duration = 50)[0].symbol_id)