from unittest import TestCase
from alphabot.Model.VolumeModel import VolumeModel
from alphabot.models import Symbol

class TestPopulateVolumeTable(TestCase):

  def test_populate_volume_table(self): #should be converted to a command later
    model = VolumeModel()
    symbols = Symbol.objects.all()
    for object in symbols:
      model.saveRecords(object.symbol, 90)
    print("I am good, can you belive it???")
    self.assertEqual(True, True)