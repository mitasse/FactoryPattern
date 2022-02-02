"""New York style pizza store concrete class"""
from ingredients.ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from pizzas.cheeze_pizza import CheesePizza
from pizzas.clam_pizza import ClamPizza
from pizzas.pepperoni_pizza import PepperoniPizza
from pizzas.pizza import Pizza
from pizzas.veggie_pizza import VeggiePizza

from stores.pizza_store import PizzaStore


class NYStylePizzaStore(PizzaStore):
    """New York style pizza store concrete class"""

    def _create_pizza(self, pizza_type: str) -> Pizza:
        """Create pizza

        Args:
            pizza_type (str): pizza type

        Returns:
            Pizza: pizza
        """
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")

        if pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")

        if pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")

        if pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza
