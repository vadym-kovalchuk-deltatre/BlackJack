# This is Snake game project

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen
from lib.snake import Snake
import time

# Screen setup
screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake: Snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.exitonclick()
