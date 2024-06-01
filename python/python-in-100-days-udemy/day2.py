print("Welcome to Sadegh day 2 pyhton in 100 days Tip Calculator")
bill = float(input("What was the total bill? $"))
percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15? %"))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay : ${
      round((round(bill, 2)/people)*(1+percentage/100), 2)}")