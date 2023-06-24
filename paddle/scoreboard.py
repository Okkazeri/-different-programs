from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.goto(position)
        self.score = -1
        self.score_growth()

    def score_growth(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'{self.score}', False, align="center", font=("Courier", 45, "normal"))
