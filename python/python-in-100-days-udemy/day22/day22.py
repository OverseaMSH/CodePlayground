from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
# functions


# functions
# setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Sadegh Udemy Python in 100 days Pong game")
screen.tracer(0)
# setup
rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(rPaddle.go_up, "Up")
screen.onkey(rPaddle.go_down, "Down")
screen.onkey(lPaddle.go_up, "w")
screen.onkey(lPaddle.go_down, "s")
game = True
level = 0.1
# setup
while game:
    time.sleep(level)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()
        level -= 0.01
    if ball.xcor() > 380:
        ball.reset_position()
    if ball.xcor() < 380:
        ball.reset_position()

screen.exitonclick()
# setup
