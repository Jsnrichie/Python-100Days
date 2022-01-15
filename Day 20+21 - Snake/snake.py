from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.speed("fastest")
            segment.setpos(x=x_pos, y=0)
            self.body.append(segment)
            x_pos -= 20


    def move(self):
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].setpos(self.body[i - 1].pos())
                # print(i)
            self.head.fd(MOVE_DISTANCE)

    def add_segment(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed("fastest")

        end_of_tail_pos = self.body[len(self.body) - 1].pos()
        segment.setpos(end_of_tail_pos)
        self.body.append(segment)

    def up(self):
        # print("Up")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # print("Down")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # print("Left")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # print("Right")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


