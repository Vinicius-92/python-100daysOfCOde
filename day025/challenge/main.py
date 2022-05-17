import pandas
import turtle
from turtle import *

data = pandas.read_csv("50_states.csv")
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = []
print_name = Turtle()
print_name.penup()
print_name.hideturtle()

guess = screen.textinput(title="Guess the state.", prompt="Name a state.").title()
while len(states) < 50:
    data_ = data[data.state == guess]
    if guess == "Exit":
        break
    if not data_.empty:
        if guess not in states:
            states.append(guess)
            print_name.goto(int(data_.x), int(data_.y))
            print_name.write(guess)
    guess = screen.textinput(title=f"{len(states)}/50 States Correct", prompt="What's another state name?").title()

states_list = data["state"].to_list()
intersect_set = list(set(states_list) - set(states))

df = pandas.DataFrame(intersect_set)
df.to_csv("states_left.csv")
