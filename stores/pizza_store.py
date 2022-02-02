"""Pizza store abstract class"""
from abc import ABC, abstractmethod

from pizzas.pizza import Pizza


class PizzaStore(ABC):
    """Pizza store abstract class"""

    @abstractmethod
    def _create_pizza(self, pizza_type: str) -> Pizza:
        """Create pizza

        Args:
            pizza_type (str): pizza type

        Returns:
            Pizza: pizza
        """

    def order_pizza(self, pizza_type: str) -> Pizza:
        """Order pizza

        Args:
            pizza_type (str): pizza type
        """
        pizza = self._create_pizza(pizza_type)
        print(f"--- Making a {pizza.get_name()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
