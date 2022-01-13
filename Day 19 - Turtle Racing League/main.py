from turtle import Turtle, Screen
from random import randint

t_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Rainbow Turtle Invitational")

user_turt = screen.textinput("Choose the Winner",
                             "Which turtle you betting on?\n (red, orange, yellow, green, blue, indigo, violet)").lower()


def setup(t_colors):
    x_pos = -240
    y_pos = -90
    for color in t_colors:
        turt = Turtle(shape="turtle")
        turt.penup()
        turt.color(color)
        turt.setpos(x_pos, y_pos)
        y_pos += 30
        turtles.append(turt)


def race(turtles):
    for i in range(100):
        for turtle in turtles:
            turtle.fd(randint(0, 20))
            if turtle.xcor() > 225:
                # print(turtle.fillcolor())
                return turtle.fillcolor()


setup(t_colors)
winner = race(turtles)
if user_turt == winner:
    print(f"You won! The {winner} turtle crossed the line first.")
else:
    print(f"You lost. The {winner} turtle crossed the line first.")

screen.exitonclick()
