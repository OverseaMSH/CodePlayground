from tkinter import *
import math

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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    titleLabel.config(text="Timer")
    checkLabel.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    count_down(WORK_MIN * 60)
    sbr=SHORT_BREAK_MIN*60
    
    lbr=LONG_BREAK_MIN*60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(lbr)
        titleLabel(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(lbr)
        titleLabel(text="Break",fg=PINK)
    else:
        count_down(lbr)
        titleLabel(text="Work",fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkLabel.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=48, bg=YELLOW)

titleLabel = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 36, "bold"), bg=YELLOW)
titleLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="python/python-in-100-days-udemy/day28/tomato.png") 
canvas.create_image(100, 112, image=tomatoImage)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

startButton = Button(text="Start", highlightthickness=0, command=start_time)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", highlightthickness=0, command=reset_timer)
resetButton.grid(column=2, row=2)

checkLabel = Label(text="", fg=GREEN, bg=YELLOW)
checkLabel.grid(column=1, row=3)

timer = None

window.mainloop()
