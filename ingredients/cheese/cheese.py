"""Cheese interface"""
from typing import Protocol


class Cheese(Protocol):
    """Cheese protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
