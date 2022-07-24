from unittest import TestCase

from alphabot.TransactionUnit.SellOptionCommand import SellOptionCommand

class TestSellOptionCommand(TestCase):

  def test_execute(self):
    command = SellOptionCommand('market')
    self.assertTrue(command.execute())