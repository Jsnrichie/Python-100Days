from turtle import Turtle

PADDLE_X = 400
SCREEN_TOP = 280
SCREEN_BOT = -280

class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.body = []
        self.create_paddle()
        self.set_position(player)
        self.top = self.body[0]
        self.bottom = self.body[-1]

    def create_paddle(self):
        y_pos = 40
        for i in range(5):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.setheading(90)
            segment.penup()
            segment.goto(x=0, y=y_pos)
            self.body.append(segment)
            y_pos -= 20

    def set_position(self, player):
        for segment in self.body:
            if player == 1:
                segment.setx(-PADDLE_X)
            else:
                segment.setx(PADDLE_X)

    def reset_paddle(self):
        y_pos = 40
        for segment in self.body:
            segment.sety(y_pos)
            y_pos -= 20


    def up(self):
        if self.top.ycor() < SCREEN_TOP:
            for segment in self.body:
                segment.fd(20)
        # print(self.top.ycor())


    def down(self):
        if self.bottom.ycor() > SCREEN_BOT:
            for segment in self.body:
                segment.bk(20)
        # print(self.bottom.ycor())




