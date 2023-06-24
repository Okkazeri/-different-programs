from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

MOVE = 20

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title("PONG")
    screen.tracer(0)

    ball = Ball()
    paddle_right = Paddle((370, 0))

    paddle_left = Paddle((-370, 0))

    first_scoreboard = Scoreboard((-70, 230))
    second_scoreboard = Scoreboard((70, 230))

    screen.listen()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        ball.move()
        screen.onkeypress(paddle_right.move_up, 'Up')
        screen.onkeypress(paddle_right.move_down, "Down")

        screen.onkeypress(paddle_left.move_up, 'w')
        screen.onkeypress(paddle_left.move_down, "s")
        # if paddle.distance(ball) < 20:
        if ball.xcor() > 360 and paddle_right.distance(ball) < 40 or ball.xcor() < -360 and paddle_left.distance(
                ball) < 40:
            ball.rotate_from_stick()
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.rotate_from_board()

        if ball.xcor() < -385:
            second_scoreboard.score_growth()
            ball.goto(0, 0)
            ball.restart()
            screen.update()
            time.sleep(0.5)
        if ball.xcor() > 385:
            first_scoreboard.score_growth()
            ball.goto(0, 0)
            ball.restart()
            screen.update()
            time.sleep(0.5)

    screen.exitonclick()
