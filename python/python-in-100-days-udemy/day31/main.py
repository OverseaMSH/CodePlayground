from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Sadegh day31 Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
cardFrontImg = PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/card_front.png")
canvas.create_image(400,263,image=cardFrontImg)
canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
crossImage=PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/wrong.png")
dontKnowBtn=Button(image=crossImage)
dontKnowBtn.grid(row=1,column=0)
checkImage=PhotoImage(
    file="python/python-in-100-days-udemy/day31/images/right.png")
knownBtn=Button(image=checkImage)
knownBtn.grid(row=1,column=1)
window.mainloop()
