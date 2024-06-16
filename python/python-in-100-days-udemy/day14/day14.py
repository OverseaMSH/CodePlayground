from db import data
from art import logo, vs
import random
import os
import sys

def new_b(g, a, b):
    return a if g == 'a' else b

def format_account(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"

def check_answer(guess, a, b):
    if a['follower_count'] > b['follower_count']:
        return guess == "a"
    else:
        return guess == "b"


def higher_lower_game():
    print(logo)
    score = 0
    should_continue = True
    b = random.choice(data)
    data.remove(b)
    a = None
    g = 'b'

    while should_continue:
        if len(data) == 0:
            print(f"Congratulations, All your guesses were correct! You won with a maximum score of {score}")
            sys.exit()
        a = new_b(g, a, b)
        b = random.choice(data)
        data.remove(b)

        print("Welcome to Sadegh Python in 100 Days Day 14 Higher Lower Game!")
        print(f"Compare A: {format_account(a)}")
        print(vs)
        print(f"Against B: {format_account(b)}")

        guess = ""
        while guess not in ['a', 'b']:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess not in ['a', 'b']:
                print("Invalid input. Please type 'A' or 'B' only!")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)

        is_correct = check_answer(guess, a, b)
        if is_correct:
            score += 1
            g = guess
            print(f"You're right! Current score: {score}")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
    higher_lower_game()
