from alphabot.TransactionUnit.OrderOperator import OrderOperator
from alphabot.TransactionUnit.PlaceOrderCommand import PlaceOrderCommand

class BuyEquityCommand(PlaceOrderCommand):
    """
    Concrete Command: Implement simple equity buying operations.
    """
    def __init__(self, payload: dict, operator: OrderOperator) -> None:
        self._payload = payload
        self._operator = operator

    def execute(self) -> bool:
        self._operator.buy(self._payload)
        print("BuyEquity is triggered and is fine")
        return True
