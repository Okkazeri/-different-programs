from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SYMBOLS = '0123456789abcdef'

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.objects = []
        self.create_snake()
        self.head = self.objects[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for turtle in range(len(self.objects) - 1, 0, -1):
            new_x = self.objects[turtle - 1].xcor()
            new_y = self.objects[turtle - 1].ycor()
            self.objects[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.speed('fastest')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.objects.append(new_turtle)

    def growth(self):
        self.add_segment(self.objects[-1].position())

    def color_generation(self):
        result = ''
        for pos in range(6):
            result += SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        return '#' + result

    def reset(self):
        for seg in self.objects:
            seg.goto(1000, 1000)
        self.objects.clear()
        self.create_snake()
        self.head = self.objects[0]