import turtle
from turtle import *
from random import choice, randint

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def draw_circle(heading_dir):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(heading_dir)


for _ in range(0, 360, 5):
    draw_circle(_)


screen = Screen()
screen.exitonclick()
