from unittest import TestCase

from OxBot.Core.TransactionUnit.SellEquityCommand import SellEquityCommand

class TestSellEquityCommand(TestCase):

  def test_execute(self):
    command = SellEquityCommand('market')
    self.assertTrue(command.execute())