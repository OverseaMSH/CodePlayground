from db import data
import random
import time
print(r"""
  ___ ___  .__         .__                    
 /   |   \ |__|  ____  |  |__    ____ _______ 
/    ~    \|  | / ___\ |  |  \ _/ __ \\_  __ \
\    Y    /|  |/ /_/  >|   Y  \\  ___/ |  | \/
 \___|_  / |__|\___  / |___|  / \___  >|__|   
    .__\/     /_____/       \/      \/        
    |  |    ____ __  _  __  ____ _______      
    |  |   /  _ \\ \/ \/ /_/ __ \\_  __ \     
    |  |__(  <_> )\     / \  ___/ |  | \/     
    |____/ \____/  \/\_/   \___  >|__|        
                               \/      
      """)
print("Welcome to Sadegh python in 100 days day 14 higher lower game!")


def compare_show(a, b, score):

    if score != 0:
        a = b
        b = random.choice(data)
        data.remove(b)
        print(f"Compare A: {a['name']}, {
            a['description']} from {a['country']}.")
        print(r"""
        ___  ________    
        \  \/ /  ___/    
         \   /\___ \     
          \_//____  > /\ 
                  \/  \/ 
          """)
        print(f"Against B: {b['name']}, {
              b['description']} from {b['country']}.")
    else:
        a = random.choice(data)
        data.remove(a)
        print(f"Compare A: {a['name']}, {
              a['description']} from {a['country']}.")
        print(r"""
        ___  ________    
        \  \/ /  ___/    
         \   /\___ \     
          \_//____  > /\ 
                  \/  \/ 
          """)
        b = random.choice(data)
        data.remove(b)
        print(f"Against B: {b['name']}, {
              b['description']} from {b['country']}.")
    return a, b


while len(data) > 0:
    score = 0
    while True:
        try:
            a, b = compare_show(a=False, b=False, score=0)
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if guess not in ['a', 'b']:
                raise ValueError
            else:
                if guess == "a":
                    if a['follower_count'] > b['follower_count']:
                        score += 1
                        print(f"You're right! Current score: {score}")
                        time.sleep(3)
                    else:
                        print(
                            f"Sorry, that's wrong. Game over! Final score: {score}")
                        break
                if guess == "b":
                    if b['follower_count'] > a['follower_count']:
                        score += 1
                        print(f"You're right! Current score: {score}")
                        time.sleep(3)
                    else:
                        print(
                            f"Sorry, that's wrong. Game over! Final score: {score}")
                        break

        except ValueError:
            print("Type 'A' or 'B'! Try again!")
