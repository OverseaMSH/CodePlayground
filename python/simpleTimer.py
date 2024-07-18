import time
from os import system,name
while True:
    selection = input("Do you want to start a new timer? (y/n) ")
    if 'y' in selection:
        hour = int(input("Enter amount of hours "))
        minute = int(input("Enter amount of minutes "))
        second = int(input("Enter amount of seconds "))
        total = hour * 60*60 + minute * 60 + second
        print("Timer is ready to go")
        time.sleep(3)
        while total > 0:
            print(total)
            total-=1
            time.sleep(1)
            if name=="nt":
                system("cls")
            else:
                system("clear")
        print("Timer ended ...")
    elif 'n' in selection:
        print("Exiting ...")
        break
    else:
        print("Invalid input. Please try again.")