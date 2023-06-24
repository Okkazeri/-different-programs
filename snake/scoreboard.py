from turtle import Turtle

with open("high_score.txt", mode="r") as high_score:
    HIGH_SCORE = int(high_score.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.high_score = HIGH_SCORE
        self.color("white")
        self.shape('classic')
        self.shapesize(stretch_len=0.1, stretch_wid=0.1)
        self.goto(0, 280)
        self.score = -1
        self.score_growth()

    def score_growth(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'You score is: {self.score} High Score: {self.high_score}', False, align="center",
                   font=("Arial", 12, "normal"))

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write('GAME OVER', False, align="center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
