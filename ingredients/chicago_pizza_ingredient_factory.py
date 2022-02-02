"""Chicago Pizza ingrediant concrete factory"""
from typing import List

from ingredients.cheese.cheese import Cheese
from ingredients.cheese.mozzarella_cheese import MozzarellaCheese
from ingredients.clams.clams import Clams
from ingredients.clams.frozen_clams import FrozenClams
from ingredients.dough.dough import Dough
from ingredients.dough.thick_crust import ThickCrust
from ingredients.pepperoni.pepperoni import Pepperoni
from ingredients.pepperoni.sliced_pepperoni import SlicedPepperoni
from ingredients.sauce.plum_tomato_sauce import PlumTomatoSauce
from ingredients.sauce.sauce import Sauce
from ingredients.veggies.black_olives import BlackOlives
from ingredients.veggies.eggplant import Eggplant
from ingredients.veggies.spinach import Spinach
from ingredients.veggies.veggies import Veggies


class ChicagoPizzaIngredientFactory:
    """Chicago Pizza ingrediant concrete factory"""

    def create_dough(self) -> Dough:
        """Create dough

        Returns:
            Dough: dough
        """
        return ThickCrust()

    def create_sauce(self) -> Sauce:
        """Create sauce

        Returns:
            Sauce: sauce
        """
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        """Create cheese

        Returns:
            Cheese: cheese
        """
        return MozzarellaCheese()

    def create_veggies(self) -> List[Veggies]:
        """Create veggies

        Returns:
            List[Veggies]: veggies list
        """
        return [BlackOlives(), Spinach(), Eggplant()]

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
        return FrozenClams()
