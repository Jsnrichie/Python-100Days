from turtle import Screen
from paddle import Paddle
from ball import Ball
from random import choice
from scoreboard import Scoreboard
import time

BOARD_WIDTH = 900
BOARD_HEIGHT = 600
UP = 5
DOWN = -5
RIGHT = 10
LEFT = -10

screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(1)
paddle_2 = Paddle(2)
scoreboard_1 = Scoreboard(1)
scoreboard_2 = Scoreboard(2)
ball = Ball()

screen.listen()
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")

up = choice([True, False])
right = choice([True, False])

game_active = True
while game_active:
    screen.update()
    time.sleep(0.025)

    if up:
        if right:
            ball.move(y_dir=UP, x_dir=RIGHT)
        else:
            ball.move(y_dir=UP, x_dir=LEFT)
    else:
        if right:
            ball.move(y_dir=DOWN, x_dir=RIGHT)
        else:
            ball.move(y_dir=DOWN, x_dir=LEFT)

    # Collision with paddle at 390
    # Hit paddle 2
    if ball.xcor() >= 375:
        if paddle_2.top.ycor() >= ball.ycor() >= paddle_2.bottom.ycor():
            right = False
        else:
            print("Paddle miss")
            if ball.xcor() >= 440:
                scoreboard_1.add_score()
                time.sleep(1)
                ball.reset_ball()
                paddle_1.reset_paddle()
                paddle_2.reset_paddle()
    elif ball.xcor() <= -375:
        if paddle_1.top.ycor() >= ball.ycor() >= paddle_1.bottom.ycor():
            right = True
        else:
            print("Paddle miss")
            if ball.xcor() <= -445:
                scoreboard_2.add_score()
                time.sleep(1)
                ball.reset_ball()
                paddle_1.reset_paddle()
                paddle_2.reset_paddle()


    # Collision with Wall
    if ball.ycor() >= 280:
        up = False
    elif ball.ycor() <= -280:
        up = True


screen.exitonclick()
