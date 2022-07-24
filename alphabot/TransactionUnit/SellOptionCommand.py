from alphabot.TransactionUnit.PlaceOrderCommand import PlaceOrderCommand

class SellOptionCommand(PlaceOrderCommand):
    """
    Concrete Command: Implement simple option selling operations.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> bool:
        #code here
        return True