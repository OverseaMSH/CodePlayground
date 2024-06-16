from db import data
from art import logo, vs
import random,os,sys

print(logo)
score = 0
shouldContinue = True
b = random.choice(data)
data.remove(b)

def format_account(a):
    return f"{a['name']}, {a['description']}, from {a['country']}"

def check_answer(guess, a, b):
    if a['follower_count'] > b['follower_count']:
        return guess == "a"
    else:
        return guess == "b"

while shouldContinue:
    if len(data)==0:
        print(f"Congratulation, All your guesses were Correct! You won with maximum score of {score}")
        sys.exit()
    print("Welcome to Sadegh python in 100 days day 14 higher lower game!")
    a = b
    b = random.choice(data)
    data.remove(b)

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

    isCorrect = check_answer(guess, a, b)
    if isCorrect:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        shouldContinue = False
        print(f"Sorry, that's wrong. Final score: {score}")
