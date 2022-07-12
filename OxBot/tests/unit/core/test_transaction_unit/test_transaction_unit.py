from unittest import TestCase

from OxBot.Core.TransactionUnit.OrderInvoker import OrderInvoker
from OxBot.Core.TransactionUnit.BuyEquityCommand import BuyEquityCommand
from OxBot.Core.TransactionUnit.OrderOperator import OrderOperator

class TestTransactionUnit(TestCase):
  
  def setUp(self):
        print("setUp: Run once to set up non-modified data for all class methods.")
        pass
  def test_buy_equity(self):
    orderDetail = {
      "symbol": "AAPL",
      "quantity": 100,
      "side": "buy",
      "type": "market",
      "duration": "day"
    }
    invoker = OrderInvoker()
    operator = OrderOperator()
    command = BuyEquityCommand(orderDetail, operator)
    invoker.invoke(command)
    self.assertTrue(command.execute())