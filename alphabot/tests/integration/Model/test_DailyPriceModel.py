import os
from django.test import TestCase
from alphabot.Model.DailyPriceModel import DailyPriceModel
from alphabot.Model.SymbolModel import SymbolModel

class TestDailyPriceModel(TestCase):
  def test_save_json_records(self):
    symbol = SymbolModel()
    path = os.path.dirname(os.path.relpath(__file__))
    data = symbol.readJson("amex_sample_tickers.json", path)
    symbol.saveRecords(data)
    model = DailyPriceModel()
    dataFrame = model.getHistoricalDataFrame('GS', 'max')
    self.assertEqual(True, model.saveRecords(dataFrame))