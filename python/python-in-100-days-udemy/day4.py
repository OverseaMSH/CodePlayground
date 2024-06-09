import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Sadegh day 4 pyhton in 100 days Rock, Paper and Scissors.")
playerChoiceNum = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computerChoiceNum = random.randint(0, 2)
if playerChoiceNum == 0:
    print("You chose:\n", rock)
elif playerChoiceNum == 1:
    print("You chose:\n", paper)
elif playerChoiceNum == 2:
    print("You chose:\n", scissors)
if computerChoiceNum == 0:
    print("Computer chose:\n", rock)
elif computerChoiceNum == 1:
    print("Computer chose:\n", paper)
elif computerChoiceNum == 2:
    print("Computer chose:\n", scissors)
if playerChoiceNum == computerChoiceNum:
    print("You Draw!")
elif playerChoiceNum == 0 and computerChoiceNum == 2 or playerChoiceNum == 1 and computerChoiceNum == 0 or playerChoiceNum == 2 and computerChoiceNum == 1:
    print("You Won!")
else:
    print("You Lost!")