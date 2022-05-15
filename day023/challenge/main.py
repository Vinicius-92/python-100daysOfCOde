import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.title("Turtler")
turtle = Player()
screen.setup(width=600, height=600)
game_is_on = True
screen.listen()
screen.onkey(fun=turtle.move, key="Up")
score = Scoreboard()
manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if turtle.ycor() > 280:
        score.update_score()
        turtle.point()
        manager.speed_up()
    manager.create_car()
    manager.move_cars()
    for car in manager.all_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
