from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake-Tiranorex game breaking 4-th wall")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.07)
        snake.move()

        if snake.head.distance(food) < 15:
            food.replaceing_food()
            snake.growth()
            scoreboard.score_growth()

        if snake.head.xcor() > 298 or snake.head.xcor() < -300 or snake.head.ycor() > 297 or snake.head.ycor() < -300:
            scoreboard.reset()
            snake.reset()

        for segment in snake.objects[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


    screen.exitonclick()
