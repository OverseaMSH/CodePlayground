from turtle import Screen, Turtle
import time
from snake import Snake
screen = Screen()
screen.setup(width=690, height=690)
screen.bgcolor("black")
screen.title("Sadegh day20 snake game")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

active = True
while active:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
