menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def get_coin():
    print("Please insert coins.")
    while True:
        try:
            while True:
                try:
                    quarters = int(input("how many quarters?: ")) * 0.25
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number of quarters.")

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
                    print("Invalid input. Please enter a valid number of nickels.")

            while True:
                try:
                    pennies = int(input("how many pennies?: ")) * 0.01
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number of pennies.")

            total = quarters + dimes + nickels + pennies
            return total

        except ValueError:
            print("Please enter a valid input.")


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(choice):
    for ingredient, amount in menu[choice]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_transaction(choice, total):
    if total >= menu[choice]["cost"]:
        change = round(total - menu[choice]['cost'], 2)
        resources["money"] += menu[choice]["cost"]
        for ingredient, amount in menu[choice]["ingredients"].items():
            resources[ingredient] -= amount
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


print("Welcome to sadegh python in 100 days day 15 coffee machine.")
while True:
    choice = input(
        "What would you like? (espresso 1.5$ / latte 2.5$ / cappuccino 3.0$):\n").lower()
    if choice == "off":
        break
    elif choice == "report":
        print_report()
    elif choice in menu:
        if check_resources(choice):
            total = get_coin()
            process_transaction(choice, total)
    else:
        print("Please enter a valid choice: espresso/latte/cappuccino")
