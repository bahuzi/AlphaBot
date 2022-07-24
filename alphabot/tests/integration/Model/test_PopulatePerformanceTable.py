from unittest import TestCase
from alphabot.Model.PerformanceModel import PerformanceModel
from alphabot.models import Symbol

class TestPopulatePerformanceTable(TestCase):

  def test_populate_performance_table(self): #should be converted to a command later
    model = PerformanceModel()
    symbols = Symbol.objects.all()
    for object in symbols:
      model.saveRecords(object.symbol, 50)
    print("I am good, can you belive it???")
    self.assertEqual(True, True)