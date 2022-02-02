"""Pizza abstract class"""
from abc import ABC, abstractmethod
from typing import List

from ingredients.cheese.cheese import Cheese
from ingredients.clams.clams import Clams
from ingredients.dough.dough import Dough
from ingredients.pepperoni.pepperoni import Pepperoni
from ingredients.sauce.sauce import Sauce
from ingredients.veggies.veggies import Veggies


class Pizza(ABC):
    """Pizza abstract class"""

    name: str

    dough: Dough
    sauce: Sauce
    veggies: List[Veggies]
    cheese: Cheese
    pepperoni: Pepperoni
    clam: Clams

    @abstractmethod
    def prepare(self) -> None:
        """Prepare"""

    def bake(self) -> None:
        """Bake"""
        print("Bake for 25 minutes at 350")

    def cut(self) -> None:
        """Cut"""
        print("Cutting the pizza into diagonal slices")

    def box(self) -> None:
        """Box"""
        print("Place pizza in official PizzaStore box")

    def get_name(self) -> str:
        """Get name"""
        return self.name

    def set_name(self, name: str) -> None:
        """Set name

        Args:
            name (str): pizza name
        """
        self.name = name
