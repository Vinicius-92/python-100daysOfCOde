import turtle
from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            y_random = randint(-250, 250)
            car.penup()
            car.color(choice(COLORS))
            car.goto(300, y_random)
            car.shapesize(stretch_len=2)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
