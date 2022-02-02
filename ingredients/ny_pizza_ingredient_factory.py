"""New York Pizza ingrediant concrete factory"""
from typing import List

from ingredients.cheese.cheese import Cheese
from ingredients.cheese.reggiano_cheese import ReggianoCheese
from ingredients.clams.clams import Clams
from ingredients.clams.fresh_clams import FreshClams
from ingredients.dough.dough import Dough
from ingredients.dough.thin_crust import ThinCrust
from ingredients.pepperoni.pepperoni import Pepperoni
from ingredients.pepperoni.sliced_pepperoni import SlicedPepperoni
from ingredients.sauce.marinara_sauce import MarinaraSauce
from ingredients.sauce.sauce import Sauce
from ingredients.veggies.garlic import Garlic
from ingredients.veggies.mushroom import Mushroom
from ingredients.veggies.onion import Onion
from ingredients.veggies.red_pepper import RedPepper
from ingredients.veggies.veggies import Veggies


class NYPizzaIngredientFactory:
    """New York Pizza ingrediant concrete factory"""

    def create_dough(self) -> Dough:
        """Create dough

        Returns:
            Dough: dough
        """
        return ThinCrust()

    def create_sauce(self) -> Sauce:
        """Create sauce

        Returns:
            Sauce: sauce
        """
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        """Create cheese

        Returns:
            Cheese: cheese
        """
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        """Create veggies

        Returns:
            List[Veggies]: veggies list
        """
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self) -> Pepperoni:
        """Create pepperoni

        Returns:
            Pepperoni: pepperoni
        """
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        """Create clam

        Returns:
            Clams: clams
        """
        return FreshClams()
