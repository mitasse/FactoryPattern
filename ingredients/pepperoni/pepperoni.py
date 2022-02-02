"""Pepperoni interface"""
from typing import Protocol


class Pepperoni(Protocol):
    """Pepperoni protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
