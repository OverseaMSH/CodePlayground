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
    deck.remove(randomCard)
    return randomCard


def is_black_jack(cards):
    secIndex = [c[1] for c in cards]
    if (1, 11) and 10 in secIndex:
        return len(cards)==2
    return False


def calculate_score(cards):
    score = 0
    aces = 0
    for card in cards:
        if isinstance(card[1], tuple):
            score += 11
            aces += 1
        else:
            score += card[1]
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score


def show_first_hand_of_player():
    print("Your cards:")
    results=[choose_card(deck),choose_card(deck)]
    for result in results:
        print(result[0])
    print("Your current score:", calculate_score(results), "\n")
    return results


def show_first_hand_of_computer():
    print("Computer cards:")
    cCard1 = choose_card(deck)
    print(cCard1[0])
    print("Computer current score:",cCard1[1][1] if isinstance(cCard1[1],tuple) else cCard1[1])
    return [cCard1]


def player_stand(computerCards):
    while calculate_score(computerCards) < 17:
        computerCards.append(choose_card(deck))
    return computerCards


while True:
    try:
        print(blackjackArt)
        print("Welcome to Sadegh python in 100 days blackjack")
        start = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if start != 'n' and start != 'y':
            raise ValueError
        else:
            if start == 'y':
                playerCards = show_first_hand_of_player()
                computerCards = show_first_hand_of_computer()
                try:
                    anotherCard = input(
                        "Type 'y' to hit or type 'n' to stand: ").lower()
                    if anotherCard != 'n' and anotherCard != 'y':
                        raise ValueError
                    else:
                        if anotherCard == 'y':
                            pass  # You can implement the 'hit' functionality here
                     
                        else:
                            computerCards = player_stand(computerCards)
                            print("Computer's final cards:")
                            for card in computerCards:
                                print(card[0])
                            print("Your final score:", calculate_score(playerCards))
                            print("Computer's final score:", calculate_score(computerCards))

                except ValueError:
                    print("Please only type 'y' or 'n'")
                break
            else:
                sys.exit()
    except ValueError:
        print("Please only type 'y' or 'n'")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
