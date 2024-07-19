from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=690, height=690)
screen.bgcolor("black")
screen.title("Sadegh day20 snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

active = True
speed = 0.1
while active:
    screen.update()
    time.sleep(speed)
    snake.move()
    if snake.head.distance(food) < 15:
        food.appear_food()
        speed -= 0.002
        score.update_score()
screen.exitonclick()
