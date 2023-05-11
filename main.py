import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_car()
    car.move_car()

    for _ in car.cars:
        if _.distance(player) < 15:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.go_to_start()
        car.next_level()
        score.increase_score()

screen.exitonclick()
