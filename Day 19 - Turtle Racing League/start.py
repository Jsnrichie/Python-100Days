# Passing a function as an argument
# def calculator(n1, n2, func):
#     return func(n1, n2) -> function called

# Etch a Sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.fd(10)


def move_bk():
    tim.bk(10)


def clockwise():
    tim.right(10)


def anti_clockwise():
    tim.left(10)


def reset():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anti_clockwise)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
