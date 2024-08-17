import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE_PATH = "python/python-in-100-days-udemy/day25/blank_states_img.gif"
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

data = pd.read_csv("python/python-in-100-days-udemy/day25/50_states.csv")
states = data.state.to_list()

guesses = []

while len(guesses) < 50:
    ask = screen.textinput(title=f"{len(guesses)}/50 States Correct",
                           prompt="What's another state's name? (Type 'Exit' to quit)").title()

    if ask is None or ask == "Exit":
        missed = [state for state in states if state not in guesses]
        pd.DataFrame(missed).to_csv("python/python-in-100-days-udemy/day25/states_to_learn.csv")
        break

    if ask in states and ask not in guesses:
        guesses.append(ask)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ask]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ask)
