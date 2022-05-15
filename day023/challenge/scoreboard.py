from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.goto(0, 260)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
