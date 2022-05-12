from turtle import *

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def create_square():
    square = Turtle("square")
    square.penup()
    square.color("white")
    return square


def add_square_to_tail(snake):
    last_square = snake.body[-1]
    new_square = create_square()
    new_square.setx(int(last_square.pos()[0]) - 20)
    snake.body.append(new_square)


class Snake:

    def __init__(self):
        self.body = []
        head = create_square()
        self.body.append(head)
        self.head = self.body[0]
        add_square_to_tail(self)
        add_square_to_tail(self)

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            self.body[seg].goto(self.body[seg - 1].pos())
        self.head.forward(MOVE_DISTANCE)

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
