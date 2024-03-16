import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    ###  write the rest of the codes ###
    while True:
        sizeinput = input("What would you like? (small/medium/large/off/report): ").lower()

        if sizeinput in ["small", "medium", "large"]:
            print("Enter Coins: ")
            sandwich_maker_instance.make_sandwich(sizeinput, recipes[sizeinput]["ingredients"])

        elif sizeinput == "off":
            break

        elif sizeinput == "report":
            for resource, number in sandwich_maker_instance.machine_resources.items():
                print(f"{resource}: {number}")

if __name__=="__main__":
    main()
