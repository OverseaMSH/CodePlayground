from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Sadegh Udemy Python in 100 days Pong game")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Key press states
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

# Functions to start and stop paddle movement
def start_r_paddle_up():
    global r_paddle_up
    r_paddle_up = True

def stop_r_paddle_up():
    global r_paddle_up
    r_paddle_up = False

def start_r_paddle_down():
    global r_paddle_down
    r_paddle_down = True

def stop_r_paddle_down():
    global r_paddle_down
    r_paddle_down = False

def start_l_paddle_up():
    global l_paddle_up
    l_paddle_up = True

def stop_l_paddle_up():
    global l_paddle_up
    l_paddle_up = False

def start_l_paddle_down():
    global l_paddle_down
    l_paddle_down = True

def stop_l_paddle_down():
    global l_paddle_down
    l_paddle_down = False

# Key bindings
screen.listen()
screen.onkeypress(start_r_paddle_up, "Up")
screen.onkeyrelease(stop_r_paddle_up, "Up")
screen.onkeypress(start_r_paddle_down, "Down")
screen.onkeyrelease(stop_r_paddle_down, "Down")
screen.onkeypress(start_l_paddle_up, "w")
screen.onkeyrelease(stop_l_paddle_up, "w")
screen.onkeypress(start_l_paddle_down, "s")
screen.onkeyrelease(stop_l_paddle_down, "s")

# Main game loop
game = True
while game:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # Move paddles based on key press states
    if r_paddle_up:
        rPaddle.go_up()
    if r_paddle_down:
        rPaddle.go_down()
    if l_paddle_up:
        lPaddle.go_up()
    if l_paddle_down:
        lPaddle.go_down()

    # Ball collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Ball collision with paddles
    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # Ball out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
