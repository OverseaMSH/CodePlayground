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
while True:
    print(art+"\n")
    print("Welcome to sadegh day 8 python in 100 days cryption app")
    selection = input(
        "Enter 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input(f"Enter the text to be {selection}d: ").lower()
    shiftNum = int(input("Enter the shift number: "))