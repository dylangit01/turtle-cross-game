from turtle import Turtle, Screen
import time

scr = Screen()
scr.listen()
MOVE_DISTANCE = 10
START_POS = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(START_POS)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def cross(self, key):
        scr.onkey(self.move_up, key)
