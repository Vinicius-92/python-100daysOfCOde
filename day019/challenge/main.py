from turtle import *
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a rainbow color: ")

colors = "red orange yellow green blue purple".split(" ")
y = -130
turtles = []
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, y)
    y += 50
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                result = "won"
            else:
                result = "lost"
            print(f"You've {result}! The {winning_color} turtle is the winner!")
        turtle.forward(randint(0, 10))

screen.exitonclick()
