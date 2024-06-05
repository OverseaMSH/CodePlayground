import time
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
            newText += alphabets[(alphabets.index(char)+shiftNum) % 26]
        else:
            newText += char
    return newText


def decrypt(text, shiftNum):
    newText = ""
    for char in text:
        newText += alphabets[(alphabets.index(char)-shiftNum) % 26]
    return newText


print(encrypt("hello", 4))
while True:
    print(art+"\n")
    print("Welcome to sadegh day 8 python in 100 days cryption app")
    selection = input(
        "Enter 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    if selection == "encode":
        text = input("Enter the text to be encoded: ").lower()
        shiftNum = int(input("Enter the shift number: "))
        print(f"Encoded text: {encrypt(text, shiftNum)}")
        finished = input("Are you finished? (yes/no): ").lower()
        if finished == 'yes':
            break
    elif selection == "decode":
        text = input("Enter the text to be decoded: ").lower()
        shiftNum = int(input("Enter the shift number: "))
        print(f"Decoded text: {decrypt(text, shiftNum)}")
        finished = input("Are you finished? (yes/no): ").lower()
        if finished == 'yes':
            break
    else:
        print("Invalid input. Please enter 'encode', 'decode'.")
        time.sleep(1)
