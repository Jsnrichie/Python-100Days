import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import choice

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(car_manager.move_cars, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    chance = [1, 2, 3, 4, 5, 6]
    if choice(chance) == 1:
        car_manager.gen_car()
    car_manager.move_cars()

    # Crosses finish line
    if player.ycor() >= FINISH_LINE_Y:
        car_manager.level += 1
        player.reset_()
        car_manager.reset_()
        scoreboard.next_level()

    # Collision with Car
    for car in car_manager.cars:
        if car.distance(player) <= 15:
            print("Collision")
            scoreboard.game_over()
            game_is_on = False








screen.exitonclick()