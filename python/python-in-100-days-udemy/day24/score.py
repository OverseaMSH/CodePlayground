from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreNum = 0
        with open("./data.txt") as data:
            self.highestScore = int(data.read())
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
            with open("./data.txt", "w") as data:
                data.write(f"{self.highestScore}")
        self.scoreNum = 0
        self.update_score()

    def increase_score(self):
        self.scoreNum += 1
        self.update_score()
