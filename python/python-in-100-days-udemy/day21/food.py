from turtle import Turtle
# from snake import Snake
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.appear_food()

    def appear_food(self):
        randomX = random.randint(-320, 320)
        randomY = random.randint(-320, 320)
        self.goto(randomX, randomY)
