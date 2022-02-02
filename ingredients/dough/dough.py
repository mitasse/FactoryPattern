"""Dough interface"""
from typing import Protocol


class Dough(Protocol):
    """Dough protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
