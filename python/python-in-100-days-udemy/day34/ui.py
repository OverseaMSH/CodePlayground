from tkinter import *
THEME_COLOR = "#375362"
class QuizInterface():
    def __init__(self,quiz_brain):
        self.quiz= quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.scoreLabel= Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.scoreLabel.grid(row=0,column=1)
        self.canvas= Canvas(width=300,height=250,bg="white")
        self.questionText= self.canvas.create_text(150,125,width=280,text="Some question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        trueImage= PhotoImage(file="python/python-in-100-days-udemy/day34/images/true.png")
        self.trueButton= Button(image=trueImage,highlightthickness=0)
        self.trueButton.grid(row=2,column=0)
        falseImage= PhotoImage(file="python/python-in-100-days-udemy/day34/images/false.png")
        self.falseButton= Button(image=falseImage,highlightthickness=0)
        self.falseButton.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.questionText,text=self.quiz.next_question())    