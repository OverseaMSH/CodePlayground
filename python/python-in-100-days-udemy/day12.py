import time
import random

art = r"""
000000    1111    222222    333333    44  44
00  00      11         2        33    44  44
00  00      11    222222    333333    444444
00  00      11    2             33        44
000000    111111  222222    333333        44

555555    666666    777777    888888    999999
55        66            77    88  88    99  99
555555    666666        77    888888    999999
    55    66  66        77    88  88        99
555555    666666        77    888888    999999
"""
print(art)
print("Welcome to Sadegh python in 100 days day12 guess number game!\n")

class RangeError(Exception):
    pass

def check_num(num, start, end, attempts):
    while attempts > 0:
        try:
            print(f"You have {attempts} remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess < start or guess > end:
                raise RangeError
            else:
                if num > guess:
                    print("Too low!")
                    attempts -= 1
                elif num < guess:
                    print("Too high!")
                    attempts -= 1
                else:
                    print(f"You got it! The answer was {guess}")
                    break
        except ValueError:
            print("Please enter an integer!")
        except RangeError:
            print(f"Please enter an integer in range of ({start},{end})!")

while True:
    try:
        numbersRange = input("Please enter a range (start,end) with a minimum difference of 15. For example (1,100): ")
        start = int(numbersRange.strip("()").split(",")[0])
        end = int(numbersRange.strip("()").split(",")[1])
        if start < end and end - start >= 15:
            while True:
                try:
                    dif = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
                    if dif not in ["easy", "hard"]:
                        raise ValueError
                    else:
                        num = random.randint(start, end)
                        if dif == "easy":
                            attempts = int((end - start) / 10)
                        else:
                            attempts = int((end - start) / 20)
                        check_num(num, start, end, attempts)
                        break
                except ValueError:
                    print("Please only type 'easy' or 'hard'!")
                    time.sleep(3)
        else:
            raise RangeError
    except ValueError:
        print("Please enter a correct range (start,end) with integers. For example (1,100)!")
        time.sleep(3)
    except RangeError:
        print(".Please enter a range with a minimum difference of 15!")
        time.sleep(3)
