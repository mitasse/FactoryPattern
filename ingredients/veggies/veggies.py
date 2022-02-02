"""Veggies interface"""
from typing import Protocol


class Veggies(Protocol):
    """Veggies protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
