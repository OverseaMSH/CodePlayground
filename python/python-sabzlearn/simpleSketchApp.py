from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_right():
    newHead = tim.heading()+10
    tim.setheading(newHead)
def turn_left():
    newHead = tim.heading()-10
    tim.setheading(newHead)
def clear_screen():
    tim.clear()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
