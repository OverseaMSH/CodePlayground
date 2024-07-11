from turtle import Turtle, Screen
import random
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple",]
yArr = [-70, -40, -10, 20, 50, 80]
turtles = []
screen.setup(width=500, height=400)
choosePrompt = "Which turtle will win the race? Enter a color: "
race=False
while True:
    try:
        choose = screen.textinput(title="Make your choice",
                                  prompt=choosePrompt)
        if choose in colors:
            for i in range(0, 6):
                newTurtle = Turtle(shape="turtle")
                newTurtle.color(colors[i])
                newTurtle.penup()
                newTurtle.goto(x=-230, y=yArr[i])
                turtles.append(newTurtle)
            race=True
            while race:
                for tur in turtles:
                    tur.forward(random.randint(0, 10))
                    if tur.xcor()>230:
                        if tur.pencolor()==choose:
                            print(f"You guessed it! {choose} turtle won the race!")
                            race=False
                        else:
                            print(f"You guessed it wrong! {tur.pencolor()} turtle won the race!")
                            race=False
            break
                            
        else:
            raise ValueError
    except ValueError:
        choosePrompt = "Please only enter 1 of these 6 colors only: red-orange-yellow-green-blue-purple"

screen.exitonclick()
