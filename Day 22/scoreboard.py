from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.set_pos(pos)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def set_pos(self, pos):
        if pos == 1:
            self.goto(x=-100, y=180)
        else:
            self.goto(x=100, y=180)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

