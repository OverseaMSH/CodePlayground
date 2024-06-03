import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Sadegh day 5 python in 100 days PyPassword Generator!")
lettersLength = int(
    input("How many letters would you like in your password?\n"))
symbolsLength = int(
    input("How many symbols would you like in your password?\n"))
numbersLength = int(
    input("How many numbers would you like in your password?\n"))
passwordArr = []
passwordArr.extend(random.choices(letters, k=lettersLength))
passwordArr.extend(random.choices(symbols, k=symbolsLength))
passwordArr.extend(random.choices(numbers, k=numbersLength))
random.shuffle(passwordArr)
print("".join(passwordArr))
