"""
The core problem (short)

In your first file (Auto) you have a manager object with a list self.autos. Each call to create_auto() creates a new Turtle object and appends that new turtle to the manager list — so move_autos() can iterate many separate turtle objects and move them each frame.

In your second file (AutoCopy) you subclass Turtle and inside create_auto() you append self to self.cars. That means each instance keeps a list that contains that same instance. This leads to one of these typical issues, depending on how you call the code:
	•	If you create one AutoCopy instance and call create_auto() once, self.cars contains only that one turtle — okay it will move, but you only have one car.
	•	If you call create_auto() multiple times on the same instance, you append the same object multiple times (not creating new turtles), which is wrong.
	•	If you instantiate multiple AutoCopy objects, each has its own cars list, so calling move_autos() on one instance will not move cars stored in other instances.

So the second file mixes the role of being a single turtle and being a manager at the same time, which causes unexpected behavior (often: no continuous movement because your move loop is iterating an empty or wrong list, or you’re only moving one turtle and not calling the move function repeatedly).
"""



from turtle import Turtle, Screen
import random

START_MOVE_DISTANCE = 5
screen = Screen()

def auto_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

class AutoCopy(Turtle):
    def __init__(self):
        super().__init__()
        screen.colormode(255)
        self.cars = []

    def create_auto(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(auto_color())
        start_y = random.randint(-150, 150)
        self.goto(400, start_y)
        self.cars.append(self)

    def move_autos(self):
        for auto in self.cars:
            auto.backward(START_MOVE_DISTANCE)