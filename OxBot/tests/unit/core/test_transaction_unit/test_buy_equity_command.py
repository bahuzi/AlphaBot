from ast import operator
from unittest import TestCase

from OxBot.Core.TransactionUnit.BuyEquityCommand import BuyEquityCommand
from OxBot.Core.TransactionUnit.OrderOperator import OrderOperator

class TestBuyEquityCommand(TestCase):

  def test_execute(self):
    operator = OrderOperator()
    command = BuyEquityCommand('market',operator)
    self.assertTrue(command.execute())