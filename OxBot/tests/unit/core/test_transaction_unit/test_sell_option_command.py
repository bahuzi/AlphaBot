from unittest import TestCase

from OxBot.Core.TransactionUnit.SellOptionCommand import SellOptionCommand

class TestSellOptionCommand(TestCase):

  def test_execute(self):
    command = SellOptionCommand('market')
    self.assertTrue(command.execute())