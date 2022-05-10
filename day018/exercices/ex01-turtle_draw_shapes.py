from tutle import *
from colors import data
from random import choice

tim = Turtle()

# Draw a dotted line
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


def draw(sides):
    angle = 360 / sides
    tim.color(choice(data))
    for side in range(sides):
        tim.forward(100)
        tim.right(angle)


for shapes_sides in range(3, 11):
    draw(shapes_sides)

screen = Screen()
screen.exitonclick()


