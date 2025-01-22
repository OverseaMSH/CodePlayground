from tkinter import *
import pandas
import random
currentCard = {}
toLearn={}
try:
    data = pandas.read_csv(
        "python/python-in-100-days-udemy/day31/data/to_learn.csv")
except FileNotFoundError:
    mainData = pandas.read_csv(
        "python/python-in-100-days-udemy/day31/data/french_words.csv")
    toLearn = mainData.to_dict(orient="records")

else:
    toLearn = data.to_dict(orient="records")


def next_card():
    global currentCard, flipTimer
    window.after_cancel(flipTimer)
    currentCard = random.choice(toLearn)
    canvas.itemconfig(cardTitle, text="French", fill="black")
    canvas.itemconfig(cardWord, text=currentCard["French"], fill="black")
    canvas.itemconfig(cardBg, image=cardFrontImg)
    flipTimer = window.after(3000, func=flip)


def is_known():
    toLearn.remove(currentCard)
    data = pandas.DataFrame(toLearn)
    data.to_csv("python/python-in-100-days-udemy/day31/data/to_learn.csv",index=False)
    next_card()


def flip():
    canvas.itemconfig(cardTitle, text="English", fill="white")
    canvas.itemconfig(cardWord, text=currentCard["English"], fill="white")
    canvas.itemconfig(cardBg, image=cardBackImg)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Sadegh day31 Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipTimer = window.after(3000, func=flip)
canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/card_front.png")
cardBackImg = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/card_back.png")
cardBg = canvas.create_image(400, 263, image=cardFrontImg)
cardTitle = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
cardWord = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
crossImage = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/wrong.png")
dontKnowBtn = Button(image=crossImage, highlightthickness=0,
                     border=0, command=next_card)
dontKnowBtn.grid(row=1, column=0)
checkImage = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/right.png")
knownBtn = Button(image=checkImage, highlightthickness=0,
                  border=0, command=is_known)
knownBtn.grid(row=1, column=1)
next_card()
window.mainloop()
