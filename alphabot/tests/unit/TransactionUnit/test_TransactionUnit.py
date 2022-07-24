from unittest import TestCase

from alphabot.TransactionUnit.OrderInvoker import OrderInvoker
from alphabot.TransactionUnit.BuyEquityCommand import BuyEquityCommand
from alphabot.TransactionUnit.OrderOperator import OrderOperator

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