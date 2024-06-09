import os
print(r"""
_____________________
|  _________________  |
| | Hello :)     0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      """)
print("Welcome to Sadegh's Python in 100 Days Day 10 Calculator Project!")
result = None
while True:
    if result is None:
        while True:
            try:
                num1 = float(input("What's the first number? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        num1 = result
    while True:
        try:
            op = input("Pick an operation (+ - * /): ").strip()
            if op in ['+', '-', '*', '/']:
                break
            else:
                raise (ValueError)
        except ValueError:
            print("Invalid operation. Please choose one of these 4 (+, -, *, /).")
    while True:
        try:
            num2 = float(input("What's the next number? "))
            if op == "/" and num2 == 0:
                raise (ZeroDivisionError)

            break
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    print(f"{num1:.2f} {op} {num2:.2f} = {result:.2f}")
    while True:
        try:
            carryOn = input(f"Type 'y' to continue with {
                            result:.2f} or type 'n' to start new calculation: ").lower()
            if carryOn == 'n':
                result = None
                os.system('cls' if os.name == 'nt' else 'clear')
                print(r"""
 _____________________
|  _________________  |
| | Hello :)     0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
                print(
                    "Welcome to Sadegh's Python in 100 Days Day 10 Calculator Project!")
                break
            elif carryOn == 'y':
                break
            else:
                raise (ValueError)
        except ValueError:
            print(
                "Invalid input. Please type 'y' to continue or 'n' to start a new calculation.")
