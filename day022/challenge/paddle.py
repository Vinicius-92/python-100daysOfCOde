from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(x=coordinates[0], y=coordinates[1])
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
