"""Clams interface"""
from typing import Protocol


class Clams(Protocol):
    """Clams protocol"""

    def to_string(self) -> str:
        """Convert to string

        Returns:
            str: name
        """
        ...
