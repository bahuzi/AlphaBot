import os
from unittest import TestCase
from alphabot.Model.DailyPriceModel import DailyPriceModel
from alphabot.Model.RSIModel import RSIModel
from alphabot.Model.VolumeModel import VolumeModel
from alphabot.models import Symbol

class TestPopulateDataTable(TestCase):
  
  def test_populate_rsi_table(self): #should be converted to a command later
    model = RSIModel()
    symbols = Symbol.objects.all()
    for object in symbols:
      # model.saveRecords(object.symbol, 5)
      model.saveRecords(object.symbol, 9)
      # model.saveRecords(object.symbol, 14)
    print("I am good, can you belive it???")
    self.assertEqual(True, True)
  
  def test_populate_volume_table(self): #should be converted to a command later
    model = VolumeModel()
    symbols = Symbol.objects.all()
    for object in symbols:
      model.saveRecords(object.symbol, 90)
    print("I am good, can you belive it???")
    self.assertEqual(True, True)
  
  
  
  
  # def test_save_json_records(self): #should be converted to a command later
  #   model = DailyPriceModel()
  #   symbols = Symbol.objects.all()
  #   for object in symbols:
  #     dataFrame = model.getHistoricalDataFrame(object.symbol, 'max')
  #     model.saveRecords(dataFrame)
  #   print("I am good, can you belive it???")
  #   self.assertEqual(True, True)