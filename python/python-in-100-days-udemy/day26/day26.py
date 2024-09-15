import pandas
data = pandas.read_csv("python/python-in-100-days-udemy/day26/nato_phonetic_alphabet.csv")
while True:
    print("Welcome to Sadegh day26 udemy python in 100 days Nato Alphabet Project")
    name = input("What's your name?\n").upper()
    phoneticDict = {row.letter: row.code for (index, row) in data.iterrows()}
    # for k in list(name):
    #     print(phoneticDict[k])
    result=[phoneticDict[k] for k in name]
    print(result)
