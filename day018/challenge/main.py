# import colorgram
import turtle
from turtle import *
from random import choice

# Colorgram extract colors form an image, first param it's the image and second is amount of colors
# colors = colorgram.extract('image.jpg', 30)
# colors_array = []
#
# for color in colors:
#     colors_array.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(colors_array)
colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.setposition(-250, -250)


def paint_ball():
    tim.dot(20, choice(colors_list))


y = -250
for _ in range(10):
    for x in range(10):
        paint_ball()
        tim.forward(50)
    tim.backward(500)
    y += 50
    tim.sety(y)

screen = Screen()
screen.exitonclick()
