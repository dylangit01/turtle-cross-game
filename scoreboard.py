from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-300, 230)
        self.score_update(self.score)

    def score_update(self, score):
        self.write(f"score:{score}", align="left", font=("Arial", 24, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.score_update(self.score)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 32, "bold"))


