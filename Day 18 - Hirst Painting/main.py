# import colorgram as cg
#
# colors = cg.extract('hirst.jpeg', 30)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

from turtle import Turtle, Screen
from random import choice

# Painting with 10x10 rows of spots
# 20 in size, spaced by 50


color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
pencil = Turtle()
screen = Screen()
screen.colormode(255)
pencil.speed("fastest")


def paint():
    pencil.penup()
    x_pos = -250
    y_pos = -200
    row = 0

    pencil.goto(x_pos, y_pos)

    while row != 10:
        for i in range(10):
            pencil.color(choice(color_list))
            pencil.dot(20)
            pencil.fd(50)
        y_pos += 50
        pencil.goto(x_pos, y_pos)
        row += 1

    pencil.color("white")


paint()
print(screen.screensize())
# pencil.dot(20)


screen.exitonclick()
