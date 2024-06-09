import time
import os

art = (
    " ,-----.                                  \n"
    "'  .--./,--,--.,---.  ,---. ,--,--.,--.--. \n"
    "|  |   ' ,-.  | .-. :(  .-'' ,-.  ||  .--' \n"
    "'  '--'\\ '-'  \\   --..-'  `) '-'  ||  |    \n"
    " `-----'`--`--'`----'`----' `--`--'`--'    \n"
    "                                            \n"
    "                                            \n"
    " ,-----.,--.       ,--.                     \n"
    "'  .--./`--' ,---. |  ,---. ,---. ,--.--.   \n"
    "|  |    ,--.| .-. ||  .-.  | .-. :|  .--'   \n"
    "'  '--'\\|  || '-' '|  | |  \\   --.|  |      \n"
    " `-----'`--'|  |-' `--' `--'`----'`--'      \n"
    "            `--'                            \n"
)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shiftNum):
    newText = ""
    for char in text:
        if char in alphabets:
            newText += alphabets[(alphabets.index(char) + shiftNum) % 26]
        else:
            newText += char
    return newText


def decrypt(text, shiftNum):
    newText = ""
    for char in text:
        if char in alphabets:
            newText += alphabets[(alphabets.index(char) - shiftNum) % 26]
        else:
            newText += char
    return newText


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art + "\n")
    print("Welcome to sadegh day 8 python in 100 days cryption app")
    try:
        selection = input(
            "Enter 'encode' to encrypt, 'decode' to decrypt:\n").lower()
        if selection == "encode":
            text = input("Enter the text to be encoded: ").lower()
            while True:
                try:
                    shiftNum = int(input("Enter the shift number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the shift.")
                    time.sleep(3)

            print(f"Encoded text: {encrypt(text, shiftNum)}")
        elif selection == "decode":
            text = input("Enter the text to be decoded: ").lower()
            while True:
                try:
                    shiftNum = int(input("Enter the shift number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the shift.")
                    time.sleep(3)

            print(f"Decoded text: {decrypt(text, shiftNum)}")
        else:
            print("Invalid input. Please enter 'encode' or 'decode'.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            continue

        while True:
            finished = input("Are you finished? (yes/no): ").lower()
            if finished == 'yes':
                break
            elif finished == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                time.sleep(3)

        if finished == 'yes':
            break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
