### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        total_ingredient = recipes[ingredients]["ingredients"]
        for ingredient, quantity in total_ingredient.items():
            if quantity > self.machine_resources[ingredient]:
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        totalamount = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
        return totalamount

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

        if coins < cost:
            print("Insufficient money")
            return False
        print("Payment is accepted")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        ingredients = recipes[sandwich_size]["ingredients"]
        #resources = resources[order_ingredients]["bread", "ham", "cheese"]

        if self.check_resources(sandwich_size):
            coins = self.process_coins()
            if self.transaction_result(coins, recipes[sandwich_size]["cost"]):
                for ingredient, amount in ingredients.items():
                    self.machine_resources[ingredient] -= amount
                print(f"{sandwich_size} is ready!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichmachine = SandwichMachine(resources)

while True:
    sizeinput = input("What would you like? (small/medium/large/off/report): ").lower()

    if sizeinput in ["small", "medium", "large"]:
        print("Enter Coins: ")
        sandwichmachine.make_sandwich(sizeinput, recipes[sizeinput]["ingredients"])

    elif sizeinput == "off":
        break

    elif sizeinput == "report":
        for resource, number in sandwichmachine.machine_resources.items():
            print(f"{resource}: {number}")
