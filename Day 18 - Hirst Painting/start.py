# IMPORTS
# import turtle
# from turtle import Turtle
# from turtle import * - imports everything

# ALIAS MODULE
# import turtle as t

# Some modules need to be installed.

from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape("triangle")
tim.color("seagreen")
# timmy_the_turtle.fd(100)
# timmy_the_turtle.right(90)

# # Draw a square
# for i in range(4):
#     tim.fd(100)
#     tim.right(90)

# # Draw a dashed line
# for _ in range(30):
#     tim.fd(5)
#     tim.penup()
#     tim.fd(5)
#     tim.pendown()

# Draw shapes
# each shape random color
# each side 100

screen = Screen()
screen.colormode(255)


# num_of_sides = 3
# while num_of_sides != 11:
#     total_deg = (num_of_sides - 2) * 180
#     angle = total_deg / num_of_sides
#     for _ in range(num_of_sides):
#         tim.fd(100)
#         tim.right(180 - angle)
#     tim.color(
#         randint(0, 255),
#         randint(0, 255),
#         randint(0, 255)
#     )
#     num_of_sides += 1


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


# # Random Walk
# tim.pen(speed=8, pensize=10)
# for _ in range(30):
#     tim.fd(randint(0, 100))
#     tim.right(choice([0, 90, 180, 270]))
#     tim.color(random_color())

# Spirograph
# radius - 100

tim.speed("fastest")

def draw_spirograph(gap):
    for _ in range(int(360/ gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(gap)

draw_spirograph(5)

screen.exitonclick()
