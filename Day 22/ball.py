from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, x_dir, y_dir):
        cur_pos_x = self.xcor()
        cur_pos_y = self.ycor()
        self.goto(x=cur_pos_x + x_dir, y=cur_pos_y + y_dir)

    def reset_ball(self):
        self.goto(0, 0)

