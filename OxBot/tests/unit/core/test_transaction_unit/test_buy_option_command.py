from unittest import TestCase

from OxBot.Core.TransactionUnit.BuyOptionCommand import BuyOptionCommand

class TestBuyOptionCommand(TestCase):

  def test_execute(self):
    command = BuyOptionCommand('market')
    self.assertTrue(command.execute())