from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_()
        self.setheading(NORTH)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def reset_(self):
        self.goto(STARTING_POSITION)
