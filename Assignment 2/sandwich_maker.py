
from data import recipes
from cashier import Cashier
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources
        self.cashier = Cashier()

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        total_ingredient = recipes[ingredients]["ingredients"]
        for ingredient, quantity in total_ingredient.items():
            if quantity > self.machine_resources[ingredient]:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        ingredients = recipes[sandwich_size]["ingredients"]
        # resources = resources[order_ingredients]["bread", "ham", "cheese"]

        if self.check_resources(sandwich_size):
            coins = self.cashier.process_coins()
            if self.cashier.transaction_result(coins, recipes[sandwich_size]["cost"]):
                for ingredient, amount in ingredients.items():
                    self.machine_resources[ingredient] -= amount
                print(f"{sandwich_size} is ready!")