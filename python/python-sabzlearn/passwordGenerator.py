import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all=lower+upper+digits+symbols
while True:
    print("Select one of the following options:\n\t1) Generate a password\n\t2) Exit the program")
    selection = input("Enter your selection: ")
    if selection == "1":
        length = int(input("Enter the length of the password: "))
        password = "".join(random.sample(all,length))
        print(password)
    elif selection == "2":
        break
    else:
        print("Invalid\nPlease try again")