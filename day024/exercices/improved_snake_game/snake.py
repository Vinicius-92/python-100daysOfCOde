from turtle import *

MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for x in STARTING_POSITIONS:
            self.add_segment(x)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            self.body[seg].goto(self.body[seg - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
