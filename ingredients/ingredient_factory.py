"""Pizza ingredient factory interface"""

from typing import List, Protocol

from ingredients.cheese.cheese import Cheese
from ingredients.clams.clams import Clams
from ingredients.dough.dough import Dough
from ingredients.pepperoni.pepperoni import Pepperoni
from ingredients.sauce.sauce import Sauce
from ingredients.veggies.veggies import Veggies


class PizzaIngredientFactory(Protocol):
    """Pizza ingredient factory interface"""

    def create_dough(self) -> Dough:
        """Create dough

        Returns:
            Dough: dough
        """
        ...

    def create_sauce(self) -> Sauce:
        """Create sauce

        Returns:
            Sauce: sauce
        """
        ...

    def create_cheese(self) -> Cheese:
        """Create cheese

        Returns:
            Cheese: cheese
        """
        ...

    def create_veggies(self) -> List[Veggies]:
        """Create veggies

        Returns:
            List[Veggies]: veggies list
        """
        ...

    def create_pepperoni(self) -> Pepperoni:
        """Create pepperoni

        Returns:
            Pepperoni: pepperoni
        """
        ...

    def create_clam(self) -> Clams:
        """Create clam

        Returns:
            Clams: clams
        """
        ...
