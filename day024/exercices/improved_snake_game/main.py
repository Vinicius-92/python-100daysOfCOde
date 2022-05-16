from turtle import Screen
import time
import snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)
game_is_on = True

screen.update()
screen.listen()


def exit_game():
    global game_is_on
    game_is_on = False


snake = snake.Snake()
food = Food()
score = ScoreBoard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(exit_game, "Escape")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect impact
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()
    # Detect impact with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    # Detect impact with your tail
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
