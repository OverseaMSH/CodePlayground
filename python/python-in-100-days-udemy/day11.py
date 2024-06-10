import random
import sys
import os
import time
blackjackArt = r"""
  ____  _            _    _            _    
 |  _ \| |          | |  (_)          | |   
 | |_) | | __ _  ___| | ___  __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                        _/ |                
                       |__/                   
  _____    _____    _____    _____
 |\ ~ /|  |\ ~ /|  |\ ~ /|  |\ ~ /|
 |}}:{{|  |}}:{{|  |}}:{{|  |}}:{{|
 |}}:{{|  |}}:{{|  |}}:{{|  |}}:{{|
 |}}:{{|  |}}:{{|  |}}:{{|  |}}:{{|
 |/_~_\|  |/_~_\|  |/_~_\|  |/_~_\|
"""


spades = [
    ("""
   _____ 
  |2    |
  |  ♠  |
  |     |
  |  ♠  |
  |____2|
         """, 2),
    ("""
   _____ 
  |3    |
  |  ♠  |
  | ♠ ♠ |
  |     |
  |____3|
         """, 3),
    ("""
   _____ 
  |4    |
  | ♠ ♠ |
  |     |
  | ♠ ♠ |
  |____4|
         """, 4),
    ("""
   _____ 
  |5    |
  | ♠ ♠ |
  |  ♠  |
  | ♠ ♠ |
  |____5|
         """, 5),
    ("""
   _____ 
  |6    |
  | ♠ ♠ |
  | ♠ ♠ |
  | ♠ ♠ |
  |____6|
         """, 6),
    ("""
   _____ 
  |7    |
  | ♠ ♠ |
  |♠ ♠ ♠|
  | ♠ ♠ |
  |____7|
         """, 7),
    ("""
   _____ 
  |8    |
  |♠ ♠ ♠|
  | ♠ ♠ |
  |♠ ♠ ♠|
  |____8|
         """, 8),
    ("""
   _____ 
  |9    |
  |♠ ♠ ♠|
  |♠ ♠ ♠|
  |♠ ♠ ♠|
  |____9|
         """, 9),
    ("""
   _____ 
  |10   |
  |♠ ♠ ♠|
  |♠ ♠ ♠|
  |♠ ♠ ♠|
  |___10|
         """, 10),
    ("""
   _____ 
  |J    |
  |♠ ♠ ♠|
  | ♠ {)|
  |♠ ♠ ♠|
  |____J|
         """, 10),
    ("""
   _____ 
  |Q    |
  |♠ ♠ ♠|
  | (.)%|
  |♠ ♠ ♠|
  |____Q|
         """, 10),
    ("""
   _____ 
  |K    |
  |♠ ♠ ♠|
  |(. %)|
  |♠ ♠ ♠|
  |____K|
         """, 10),
    ("""
   _____ 
  |A    |
  |     |
  |  ♠  |
  |     |
  |____A|
         """, (1, 11)),
]
hearts = [
    ("""
   _____ 
  |2    |
  |  ♥  |
  |     |
  |  ♥  |
  |____2|
         """, 2),
    ("""
   _____ 
  |3    |
  |  ♥  |
  | ♥ ♥ |
  |     |
  |____3|
         """, 3),
    ("""
   _____ 
  |4    |
  | ♥ ♥ |
  |     |
  | ♥ ♥ |
  |____4|
         """, 4),
    ("""
   _____ 
  |5    |
  | ♥ ♥ |
  |  ♥  |
  | ♥ ♥ |
  |____5|
         """, 5),
    ("""
   _____ 
  |6    |
  | ♥ ♥ |
  | ♥ ♥ |
  | ♥ ♥ |
  |____6|
         """, 6),
    ("""
   _____ 
  |7    |
  | ♥ ♥ |
  |♥ ♥ ♥|
  | ♥ ♥ |
  |____7|
         """, 7),
    ("""
   _____ 
  |8    |
  |♥ ♥ ♥|
  | ♥ ♥ |
  |♥ ♥ ♥|
  |____8|
         """, 8),
    ("""
   _____ 
  |9    |
  |♥ ♥ ♥|
  |♥ ♥ ♥|
  |♥ ♥ ♥|
  |____9|
         """, 9),
    ("""
   _____ 
  |10   |
  |♥ ♥ ♥|
  |♥ ♥ ♥|
  |♥ ♥ ♥|
  |___10|
         """, 10),
    ("""
   _____ 
  |J    |
  |♥ ♥ ♥|
  | ♥ {)|
  |♥ ♥ ♥|
  |____J|
         """, 10),
    ("""
   _____ 
  |Q    |
  |♥ ♥ ♥|
  | (.)%|
  |♥ ♥ ♥|
  |____Q|
         """, 10),
    ("""
   _____ 
  |K    |
  |♥ ♥ ♥|
  |(. %)|
  |♥ ♥ ♥|
  |____K|
         """, 10),
    ("""
   _____ 
  |A    |
  |     |
  |  ♥  |
  |     |
  |____A|
         """, (1, 11)),
]
diamonds = [
    ("""
   _____ 
  |2    |
  |  ♦  |
  |     |
  |  ♦  |
  |____2|
         """, 2),
    ("""
   _____ 
  |3    |
  |  ♦  |
  | ♦ ♦ |
  |     |
  |____3|
         """, 3),
    ("""
   _____ 
  |4    |
  | ♦ ♦ |
  |     |
  | ♦ ♦ |
  |____4|
         """, 4),
    ("""
   _____ 
  |5    |
  | ♦ ♦ |
  |  ♦  |
  | ♦ ♦ |
  |____5|
         """, 5),
    ("""
   _____ 
  |6    |
  | ♦ ♦ |
  | ♦ ♦ |
  | ♦ ♦ |
  |____6|
         """, 6),
    ("""
   _____ 
  |7    |
  | ♦ ♦ |
  |♦ ♦ ♦|
  | ♦ ♦ |
  |____7|
         """, 7),
    ("""
   _____ 
  |8    |
  |♦ ♦ ♦|
  | ♦ ♦ |
  |♦ ♦ ♦|
  |____8|
         """, 8),
    ("""
   _____ 
  |9    |
  |♦ ♦ ♦|
  |♦ ♦ ♦|
  |♦ ♦ ♦|
  |____9|
         """, 9),
    ("""
   _____ 
  |10   |
  |♦ ♦ ♦|
  |♦ ♦ ♦|
  |♦ ♦ ♦|
  |___10|
         """, 10),
    ("""
   _____ 
  |J    |
  |♦ ♦ ♦|
  | ♦ {)|
  |♦ ♦ ♦|
  |____J|
         """, 10),
    ("""
   _____ 
  |Q    |
  |♦ ♦ ♦|
  | (.)%|
  |♦ ♦ ♦|
  |____Q|
         """, 10),
    ("""
   _____ 
  |K    |
  |♦ ♦ ♦|
  |(. %)|
  |♦ ♦ ♦|
  |____K|
         """, 10),
    ("""
   _____ 
  |A    |
  |     |
  |  ♦  |
  |     |
  |____A|
         """, (1, 11)),
]
clubs = [
    ("""
   _____ 
  |2    |
  |  ♣  |
  |     |
  |  ♣  |
  |____2|
         """, 2),
    ("""
   _____ 
  |3    |
  |  ♣  |
  | ♣ ♣ |
  |     |
  |____3|
         """, 3),
    ("""
   _____ 
  |4    |
  | ♣ ♣ |
  |     |
  | ♣ ♣ |
  |____4|
         """, 4),
    ("""
   _____ 
  |5    |
  | ♣ ♣ |
  |  ♣  |
  | ♣ ♣ |
  |____5|
         """, 5),
    ("""
   _____ 
  |6    |
  | ♣ ♣ |
  | ♣ ♣ |
  | ♣ ♣ |
  |____6|
         """, 6),
    ("""
   _____ 
  |7    |
  | ♣ ♣ |
  |♣ ♣ ♣|
  | ♣ ♣ |
  |____7|
         """, 7),
    ("""
   _____ 
  |8    |
  |♣ ♣ ♣|
  | ♣ ♣ |
  |♣ ♣ ♣|
  |____8|
         """, 8),
    ("""
   _____ 
  |9    |
  |♣ ♣ ♣|
  |♣ ♣ ♣|
  |♣ ♣ ♣|
  |____9|
         """, 9),
    ("""
   _____ 
  |10   |
  |♣ ♣ ♣|
  |♣ ♣ ♣|
  |♣ ♣ ♣|
  |___10|
         """, 10),
    ("""
   _____ 
  |J    |
  |♣ ♣ ♣|
  | ♣ {)|
  |♣ ♣ ♣|
  |____J|
         """, 10),
    ("""
   _____ 
  |Q    |
  |♣ ♣ ♣|
  | (.)%|
  |♣ ♣ ♣|
  |____Q|
         """, 10),
    ("""
   _____ 
  |K    |
  |♣ ♣ ♣|
  |(. %)|
  |♣ ♣ ♣|
  |____K|
         """, 10),
    ("""
   _____ 
  |A    |
  |     |
  |  ♣  |
  |     |
  |____A|
         """, (1, 11)),
]
deck = spades + hearts + diamonds + clubs

def choose_card(deck):
    random.shuffle(deck)
    randomCard = random.choice(deck)
    if randomCard[1] == (1, 11):
        if randomCard[1] + 11 > 21:
            randomCard = (randomCard[0], 1)
        else:
            randomCard = (randomCard[0], 11)
    deck.remove(randomCard)
    return randomCard



def show_first_hand_of_player():
    print("Your cards:")
    pCard1, pCard2 = choose_card(deck), choose_card(deck)
    print(pCard1[0], pCard2[0])
    print("Current score:", pCard1[1] + pCard2[1], "\n")
    return [pCard1, pCard2]

def show_first_hand_of_computer():
    print("Computer cards:")
    cCard1 = choose_card(deck)
    print(cCard1[0])
    return [cCard1]

def player_stand(computerCards, playerCards):
    while sum(card[1] for card in computerCards) < 22:
        computerCards.append(choose_card(deck))
    return computerCards

while True:
    try:
        print(blackjackArt)
        print("Welcome to Sadegh python in 100 days blackjack")
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if start != 'n' and start != 'y':
            raise ValueError
        else:
            if start == 'y':
                playerCards = show_first_hand_of_player()
                computerCards = show_first_hand_of_computer()
                try:
                    anotherCard = input("Type 'y' to hit or type 'n' to stand: ").lower()
                    if anotherCard != 'n' and anotherCard != 'y':
                        raise ValueError
                    else:
                        if anotherCard == 'y':
                            pass  # You can implement the 'hit' functionality here
                        else:
                            computerCards = player_stand(computerCards, playerCards)
                            print("Computer's final cards:")
                            for card in computerCards:
                                print(card[0])
                            print("Computer's final score:", sum(card[1] for card in computerCards))
                            print("Your final score:", sum(card[1] for card in playerCards))

                except ValueError:
                    print("Please only type 'y' or 'n'")
                break
            else:
                sys.exit()
    except ValueError:
        print("Please only type 'y' or 'n'")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')