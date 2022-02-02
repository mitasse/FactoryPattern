"""Clam pizza concrete class"""
from ingredients.ingredient_factory import PizzaIngredientFactory

from pizzas.pizza import Pizza


class ClamPizza(Pizza):
    """Clam pizza concrete class"""

    def __init__(self, ingredient_factory) -> None:
        self.ingredient_factory: PizzaIngredientFactory = ingredient_factory

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        print(f"Tossing {self.dough.to_string()}...")
        self.sauce = self.ingredient_factory.create_sauce()
        print(f"Adding {self.sauce.to_string()}...")
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()
        print("Adding toppings:")
        for topping in [self.cheese, self.clam]:
            print(f"    {topping.to_string()}")
