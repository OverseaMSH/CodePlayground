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
result= None
while True:
    if result is None:
        while True:
            try:
                num1=float(input("What's the first number? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        