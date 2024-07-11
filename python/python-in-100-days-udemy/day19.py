from turtle import Turtle, Screen

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple",]
yArr = [-70, -40, -10, 20, 50, 80]
screen.setup(width=500, height=400)
choose = screen.textinput(title="Make your choice",
                          prompt="Which turtle will win the race? Enter a color: ")

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=yArr[i])
screen.exitonclick()
