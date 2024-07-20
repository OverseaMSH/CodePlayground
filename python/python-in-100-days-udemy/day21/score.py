from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreNum = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write(f"Score: {self.scoreNum}", align="center",
                   font=("Roboto", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.scoreNum += 1
        self.clear()
        self.write(f"Score: {self.scoreNum}", align="center",
                   font=("Roboto", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center",
                   font=("Roboto", 24, "normal"))
