from turtle import Turtle, Screen
import random

START_MOVE_DISTANCE = 5
screen = Screen()

def auto_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

class Auto:
    def __init__(self):
        screen.colormode(255)
        self.autos = []
        # self.create_auto()
        # self.x_move = 10

    def create_auto(self):
        car = Turtle('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(auto_color())
        start_y = random.randint(-120, 120)
        car.goto(400, start_y)
        self.autos.append(car)

    def move_autos(self):
        for auto in self.autos:
            auto.backward(START_MOVE_DISTANCE)
