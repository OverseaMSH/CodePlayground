from turtle import Screen, Turtle
from paddle import Paddle
# functions



# functions
# setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Sadegh Udemy Python in 100 days Pong game")
screen.tracer(0)
# setup
rPaddle = Paddle((350,0))
lPaddle = Paddle((-350,0))


screen.listen()
screen.onkey(rPaddle.go_up, "Up")
screen.onkey(rPaddle.go_down, "Down")
screen.onkey(lPaddle.go_up, "w")
screen.onkey(lPaddle.go_down, "s")
game=True
# setup
while game:
    screen.update()
screen.exitonclick()
# setup
