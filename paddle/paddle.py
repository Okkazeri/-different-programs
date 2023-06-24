from turtle import Turtle

MOVE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setpos(position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=0.5)

    def move_up(self):
        x_cor = self.xcor()
        y_xor = self.ycor()
        self.goto(x_cor, y_xor + MOVE)

    def move_down(self):
        x_cor = self.xcor()
        y_xor = self.ycor()
        self.goto(x_cor, y_xor - MOVE)
