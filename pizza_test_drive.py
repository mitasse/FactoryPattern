"""Main function"""
from stores.chicago_store import ChicagoStylePizzaStore
from stores.ny_store import NYStylePizzaStore


def main() -> None:
    """Main function"""
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.get_name()}\n")

    pizza = ny_store.order_pizza("clam")
    print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza.get_name()}\n")

    pizza = ny_store.order_pizza("pepperoni")
    print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza.get_name()}\n")

    pizza = ny_store.order_pizza("veggie")
    print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza.get_name()}\n")


if __name__ == "__main__":
    main()
