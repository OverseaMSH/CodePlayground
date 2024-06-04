import random
import os
print(r"""
 _   _
| | | |
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/   

Welcome to sadegh day 7 python in 100 days Hangman
""")

wordCategories = {
    "fruits": [
        "apple", "banana", "orange", "grape", "kiwi", "strawberry", "pineapple",
        "watermelon", "blueberry", "peach", "mango", "pear", "cherry", "lemon",
        "lime", "coconut", "apricot", "fig", "plum", "papaya", "raspberry",
        "blackberry", "cranberry", "melon"
    ],
    "animals": [
        "dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra", "monkey",
        "panda", "kangaroo", "koala", "crocodile", "hippopotamus", "rhinoceros",
        "cheetah", "bear", "wolf", "fox", "rabbit", "deer", "squirrel", "horse",
        "cow", "pig"
    ],
    "colors": [
        "red", "orange", "yellow", "green", "blue", "purple", "pink", "brown",
        "black", "white", "gray", "silver", "gold", "beige", "maroon", "cyan",
        "magenta", "olive", "teal", "navy"
    ],
    "countries": [
        "usa", "canada", "mexico", "brazil", "argentina", "uk", "france", "germany",
        "italy", "spain", "russia", "china", "japan", "india", "australia",
        "southafrica", "egypt", "nigeria", "kenya", "saudiarabia", "unitedarabemirates",
        "turkey", "iran", "pakistan"
    ],
    "vehicles": [
        "car", "bus", "truck", "motorcycle", "bicycle", "train", "airplane",
        "helicopter", "boat", "submarine", "ship", "scooter", "van", "ambulance",
        "firetruck", "policecar", "tractor", "forklift", "jet", "spaceship"
    ],
    "professions": [
        "doctor", "teacher", "engineer", "lawyer", "artist", "chef", "scientist",
        "programmer", "writer", "musician", "actor", "athlete", "pilot", "policeofficer",
        "firefighter", "nurse", "dentist", "architect", "veterinarian", "farmer"
    ],
    "sports": [
        "soccer", "basketball", "football", "tennis", "volleyball", "golf",
        "cricket", "baseball", "swimming", "running", "cycling", "boxing",
        "rugby", "hockey", "skiing", "snowboarding", "surfing", "skateboarding",
        "wrestling", "gymnastics"
    ],
    "foods": [
        "pizza", "hamburger", "spaghetti", "sushi", "sandwich", "salad", "steak",
        "chicken", "soup", "rice", "taco", "burrito", "pasta", "pancake", "waffle",
        "omelette", "burger", "fries", "hotdog", "popcorn"
    ],
    "movies": [
        "avatar", "titanic", "starwars", "thelordoftherings", "harrypotter",
        "jurassicpark", "thematrix", "forrestgump", "thegodfather", "inception",
        "thelionking", "frozen", "findingnemo", "toystory", "backtothefuture",
        "thedarkknight", "pulpfiction", "theshawshankredemption", "fightclub",
        "interstellar"
    ],
    "languages": [
        "english", "spanish", "french", "german", "chinese", "arabic", "russian",
        "japanese", "portuguese", "italian", "korean", "dutch", "turkish",
        "swedish", "polish", "hindi", "greek", "hebrew", "thai", "vietnamese"
    ],
    "emotions": [
        "happy", "sad", "angry", "excited", "nervous", "surprised", "fearful",
        "disgusted", "content", "confused", "bored", "loved", "hated", "jealous",
        "relaxed", "stressed", "hopeful", "proud", "shy", "embarrassed"
    ]
}

hangmanStages = [
    r"""
      +---+
          |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]


def select_random_word(dict):
    category = random.choice(list(dict.keys()))
    word = random.choice(dict[category])
    return category, word
def find_indexes(string,character):
    indexes=[index for index,char in enumerate(string) if char==character] 
    return indexes
    # Find index of the letters guessed by the user that are in the word. For example our word is toystory and the guessed letter is y. It will return the y indexes as list in toystory.
print(find_indexes("toystory","y"))
category, word = select_random_word(wordCategories)
guessedWord = []
for i in word:
    guessedWord.append("_")
counter = 0
hangmanStage = 0
while True:
    for i in guessedWord:
        if i == "_":
            counter += 1
    # guessedLetter = input(f"Guess a letter, the word is in {category} category : ")
    # os.system('cls' if os.name == 'nt' else 'clear')
        