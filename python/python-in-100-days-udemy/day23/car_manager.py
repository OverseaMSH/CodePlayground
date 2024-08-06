from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.carSpeed = 10
    def create_car(self):
        randomeChance=random.randint(1,6)
        if randomeChance==1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1,stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY=random.randint(-250,250)
            newCar.goto(300,randomY)
            self.allCars.append(newCar)
    def move_cars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)
    def level_up(self):
        self.carSpeed+=MOVE_INCREMENT