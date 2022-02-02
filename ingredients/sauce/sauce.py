"""Sauce interface"""
from typing import Protocol


class Sauce(Protocol):
    """Sauce protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
