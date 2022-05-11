import turtle
from turtle import *
from random import choice, randint

turtle.colormode(255)

tim = Turtle()
tim.pensize(10)
tim.speed("fastest")
angles = "0 90 180 270 360".split(" ")


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def draw(angle):
    rgb_color = random_color()
    tim.pencolor(rgb_color)
    tim.setheading(angle)
    tim.forward(30)


for _ in range(200):
    draw(int(choice(angles)))

screen = Screen()
screen.exitonclick()
