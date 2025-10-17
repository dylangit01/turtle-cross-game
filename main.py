from turtle import Screen
from auto import Auto
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing Project")
screen.tracer(0)

new_auto = Auto()
player = Player()
sco = Scoreboard()

is_game_on = True
score = 0
pass_time = 0.2

while is_game_on:
    time.sleep(pass_time)
    screen.update()
    player.cross('Up')
    new_auto.create_auto()
    new_auto.move_autos()
    for auto in new_auto.autos:
        if player.distance(auto) < 20:
            sco.game_over()
            is_game_on = False
    if player.is_at_finish_line():
        sco.add_score()
        player.back_to_start()
        pass_time *= 0.5

screen.exitonclick()