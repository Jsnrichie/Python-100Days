from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WEST = 180


class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 1

    def gen_car(self):
        y_pos = randint(-260, 260)
        x_pos = 300
        car = Turtle(shape="square")
        car.color(choice(COLORS))
        car.penup()
        car.setheading(WEST)

        car.sety(y_pos)
        car.setx(x_pos)

        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.fd(STARTING_MOVE_DISTANCE + ((self.level - 1) * MOVE_INCREMENT))

        # for car in self.cars:
        #     x_pos = car.xcor()
        #     y_pos = car.ycor()
        #     distance_x = -(STARTING_MOVE_DISTANCE + ((self.level - 1) * MOVE_INCREMENT))
        #     car.goto(x= (x_pos + distance_x), y=y_pos)


    def reset_(self):
        for car in self.cars:
            car.ht()
        self.cars = []

