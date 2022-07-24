
from alphabot.TransactionUnit.PlaceOrderCommand import PlaceOrderCommand


class OrderInvoker:
    """
    The OrderInvoker (Invoker) class is associated with one or several commands. It sends a request to the command
    """
    _command = None
    
    def invoke(self, command: PlaceOrderCommand) -> None:
        self._command = command
        self._command.execute()
        print('invoker is working', command)