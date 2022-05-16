from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


def get_high_score():
    with open("score.txt") as file:
        score = file.read()
        return int(score)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def set_high_score(self):
        with open("score.txt", mode="w") as file:
            file.write(str(self.high_score))
