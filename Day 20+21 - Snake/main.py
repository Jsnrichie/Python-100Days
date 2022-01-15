import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Slytherin")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

alive = True
while alive:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("he EATIN")
        food.refresh()
        scoreboard.increase_score()
        snake.add_segment()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        alive = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.body[1:-1]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            alive = False
            scoreboard.game_over()


screen.exitonclick()
