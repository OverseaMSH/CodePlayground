from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodro")
window.config(padx=100, pady=48, bg=YELLOW)
titleLabel = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"))
titleLabel.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(
    file="python/python-in-100-days-udemy/day28/tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
startButton = Button(text="Start", highlightthickness=0)
startButton.grid(column=0, row=2)
resetButton = Button(text="Reset", highlightthickness=0)
resetButton.grid(column=2, row=2)
checkLabel = Label(text="✔", fg=GREEN,bg=YELLOW)
checkLabel.grid(column=1, row=3)
window.mainloop()
