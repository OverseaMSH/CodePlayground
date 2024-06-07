import os
print("Welcome to Sadegh day 9 pyhton in 100 days First price blind auction.\n")
bids = {}
while True:
    name = input("What's your name? : ")
    bid = int(input("What's your bid? : $"))
    bids[name] = bid
    nextBidder = input(
        "Are there any other bidders? Type 'yes' or 'no'?\n").lower()
    if nextBidder == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif nextBidder == "no":
        print(f"The winner is {max(bids, key=bids.get)} with a bid of ${bids[max(bids, key=bids.get)]}")
        break
