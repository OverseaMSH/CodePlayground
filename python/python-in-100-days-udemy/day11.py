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
    aceCounter, tenCounter = 0, 0
    for card in cards:
        if card[1] == 10:
            tenCounter += 1
        if card[1] == (1, 11):
            aceCounter += 1
    if len(cards) == 2 and aceCounter == 1 and tenCounter == 1:
        return True
    else:
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


def check_winner(playerCards, computerCards):
    playerScore = calculate_score(playerCards)
    computerScore = calculate_score(computerCards)

    if playerScore == computerScore:
        print("Draw!")
    elif playerScore > 21:
        print("Player busted! Computer won!")
    elif computerScore > 21:
        print("Computer busted! Player won!")
    elif playerScore > computerScore:
        print("Player won!")
    else:
        print("Computer won!")


def show_first_hand_of_player():
    print("=" * 40)
    print("Player cards:")
    results = [choose_card(deck), choose_card(deck)]
    for result in results:
        print(result[0])
    print("Your current score:", calculate_score(results), "\n")
    return results, is_black_jack(results)


def player_hit(playerCards, computerCards):
    playerCards.append(choose_card(deck))
    print("Computer's final cards:")
    for card in computerCards:
        print(card[0])
    print("Computer's final score:", calculate_score(computerCards))
    for card in playerCards:
        print(card[0])
    print("Player final score:", calculate_score(playerCards))
    if is_black_jack(computerCards):
        print("Computer has Blackjack! Computer won!\n")
        print("=" * 40)
        time.sleep(3)
    return playerCards


def show_first_hand_of_computer():
    print("Computer cards:")
    cCard1 = choose_card(deck)
    print(cCard1[0])
    print("Computer current score:", cCard1[1][1] if isinstance(cCard1[1], tuple) else cCard1[1])
    return [cCard1]


def player_stand(computerCards, playerCards):
    while calculate_score(computerCards) < 17:
        computerCards.append(choose_card(deck))
    print("Computer's final cards:")
    for card in computerCards:
        print(card[0])
    print("Computer's final score:", calculate_score(computerCards))
    for card in playerCards:
        print(card[0])
    print("Player final score:", calculate_score(playerCards))
    if is_black_jack(computerCards):
        print("Computer has Blackjack! Computer won!\n")
        print("=" * 40)
        time.sleep(3)
    return computerCards


def play_blackjack():
    while True:
        try:
            print(blackjackArt)
            print("Welcome to Sadegh python in 100 days blackjack")
            start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
            if start != 'n' and start != 'y':
                raise ValueError
            elif start == 'y':
                computerCards = show_first_hand_of_computer()
                playerFirst = show_first_hand_of_player()
                playerCards = playerFirst[0]
                if playerFirst[1]:
                    print("Player has Blackjack! Player won!\n")
                    print("=" * 40)
                    time.sleep(3)
                    continue
                else:
                    while True:
                        try:
                            anotherCard = 'y'
                            while anotherCard == 'y' and calculate_score(playerCards) <= 21:
                                anotherCard = input("Type 'y' to hit or type 'n' to stand: ").lower()
                                if anotherCard != 'n' and anotherCard != 'y':
                                    raise ValueError
                                if anotherCard == 'y':
                                    playerCards = player_hit(playerCards, computerCards)
                            computerCards = player_stand(computerCards, playerCards)
                            check_winner(playerCards, computerCards)
                            break  # Start a new game after the current game ends
                        except ValueError:
                            print("Please only type 'y' or 'n'")
                            time.sleep(3)
            else:
                sys.exit()
        except ValueError:
            print("Please only type 'y' or 'n'")
            time.sleep(3)


play_blackjack()