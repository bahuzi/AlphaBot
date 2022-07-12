
class OrderOperator:
    """
    The OrderOperator (Receiver) class contain important business logic. This is where the actual work performs
    """

    def buy(self, a: dict) -> bool:
        print(f"\nReceiver: Working on ({a}.)", end="")
        return True

    def sell(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")
    
    def save(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")