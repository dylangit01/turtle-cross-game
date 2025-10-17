from turtle import Screen
from auto import Auto
from player import Player
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Project")
screen.tracer(0)

new_auto = Auto()
player = Player()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    player.cross('Up')
    new_auto.create_auto()
    new_auto.move_autos()

screen.exitonclick()