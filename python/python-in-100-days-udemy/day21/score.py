from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreNum = 0
        self.highestScore = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write(f"Score: {self.scoreNum}", align="center",
                   font=("Roboto", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.scoreNum} Highest score: {self.highestScore}", align="center",
                   font=("Roboto", 24, "normal"))

    def restart(self):
        if self.scoreNum > self.highestScore:
            self.highestScore = self.scoreNum
        self.scoreNum = 0
        self.update_score()
    def increase_score(self):
        self.scoreNum += 1
        self.update_score()

