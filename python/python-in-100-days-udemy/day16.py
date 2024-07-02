class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"water": 50, "coffee": 18}),
            MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("cappuccino", 3.0, {
                     "water": 250, "milk": 100, "coffee": 24})
        ]

    def get_items(self):
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for ingredient, amount in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, order):
        for ingredient, amount in order.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Here is your {order.name}. Enjoy!")


class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def make_payment(self, cost):
        print("Please insert coins.")
        total = self.process_coins()
        if total >= cost:
            change = round(total - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def process_coins(self):
        while True:
            try:
                while True:
                    try:
                        quarters = int(input("how many quarters?: ")) * 0.25
                        break
                    except ValueError:
                        print(
                            "Invalid input. Please enter a valid number of quarters.")

                while True:
                    try:
                        dimes = int(input("how many dimes?: ")) * 0.10
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number of dimes.")

                while True:
                    try:
                        nickels = int(input("how many nickels?: ")) * 0.05
                        break
                    except ValueError:
                        print(
                            "Invalid input. Please enter a valid number of nickels.")

                while True:
                    try:
                        pennies = int(input("how many pennies?: ")) * 0.01
                        break
                    except ValueError:
                        print(
                            "Invalid input. Please enter a valid number of pennies.")

                total = quarters + dimes + nickels + pennies
                return total

            except ValueError:
                print("Please enter a valid input.")


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        try:
            choice = input(f"What would you like? (espresso 1.5$ / latte 2.5$ / cappuccino 3.0$\n").lower()
        except KeyboardInterrupt:
            print("\nProgram terminated.")
            break

        if choice == "off":
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                print(
                    "Please enter a valid choice: espresso 1.5$ / latte 2.5$ / cappuccino 3.0$")


if __name__ == "__main__":
    main()
