from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x= -220, y=270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



