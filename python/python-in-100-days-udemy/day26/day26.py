import pandas as pd
import time
data = pd.read_csv(
    "python/python-in-100-days-udemy/day26/nato_phonetic_alphabet.csv")
phoneticDict = {row.letter: row.code for (index, row) in data.iterrows()}
while True:
    print("Welcome to Sadegh day26 udemy python in 100 days Nato Alphabet Project")
    name = input("What's your name?\n").upper()
    if not name:
        print("Empty input detected. Exiting program.")
        time.sleep(3)
        break
    try:
        if not name.isalpha():
            raise ValueError("Name should contain only alphabetic characters.")

        result = [phoneticDict[k] for k in name]
        print(result)

    except KeyError:
        print("An error occurred: One or more letters are missing from the phonetic dictionary.")

    except ValueError as ve:
        print(f"Invalid input: {ve}. Exiting program.")
        break
