from __future__ import annotations
from abc import ABC, abstractmethod


class PlaceOrderCommand(ABC):
    """
    The PlaceOrderCommand interface declares a method for executing a command.
    """
    @abstractmethod
    def execute(self) -> None:
        pass    
