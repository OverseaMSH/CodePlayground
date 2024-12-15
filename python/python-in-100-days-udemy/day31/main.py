from tkinter import *
import pandas
import random
data = pandas.read_csv(
    "python/python-in-100-days-udemy/day31/data/french_words.csv")
data = data.to_dict(orient="records")


def next_card():
    currentCard = random.choice(data)
    canvas.itemconfig(cardTitle, text="French")
    canvas.itemconfig(cardWord, text=currentCard["French"])


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Sadegh day31 Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/card_front.png")
canvas.create_image(400, 263, image=cardFrontImg)
cardTitle = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
cardWord = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
crossImage = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/wrong.png")
dontKnowBtn = Button(image=crossImage, highlightthickness=0,border=0, command=next_card)
dontKnowBtn.grid(row=1, column=0)
checkImage = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/right.png")
knownBtn = Button(image=checkImage, highlightthickness=0,border=0, command=next_card)
knownBtn.grid(row=1, column=1)
next_card()
window.mainloop()
