from turtle import Turtle
import random

MOVING_LIST = [7, -7]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.growth_x = -0.5
        self.growth_y = 0.5
        self.move_x = -7
        self.move_y = 7
        self.color("white")
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def move(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        self.goto(x_cor + self.move_x, y_cor + self.move_y)

    def rotate_from_stick(self):
        self.move_x += self.growth_x
        self.move_x *= -1
        self.growth_x *= -1

    def rotate_from_board(self):
        self.move_y += self.growth_y
        self.move_y *= -1
        self.growth_y *= -1

    def restart(self):
        self.move_x = random.choice(MOVING_LIST)
        if self.move_x > 0:
            self.growth_x = 1
        else:
            self.growth_x = -1

        self.move_y = random.choice(MOVING_LIST)
        if self.move_y > 0:
            self.growth_y = 1
        else:
            self.growth_y = -1
