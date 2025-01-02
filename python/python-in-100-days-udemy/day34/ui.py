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
        self.trueButton= Button(image=trueImage,highlightthickness=0,command=self.true_pressed)
        self.trueButton.grid(row=2,column=0)
        falseImage= PhotoImage(file="python/python-in-100-days-udemy/day34/images/false.png")
        self.falseButton= Button(image=falseImage,highlightthickness=0,command=self.false_pressed)
        self.falseButton.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
            question_text=self.quiz.next_question()
            self.canvas.itemconfig(self.questionText,text=question_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.questionText,text="You've reached the end of the quiz")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        isRight=self.quiz.check_answer("False")
        self.give_feedback(isRight)
        

    def give_feedback(self,isRight):
        if isRight:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)