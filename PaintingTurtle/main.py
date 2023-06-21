from turtle import Turtle, Screen, colormode
import random


def _random_color() -> int:
    return random.randint(0, 250)


def get_color() -> tuple[int, int, int]:
    return _random_color(), _random_color(), _random_color()


def set_directions() -> list[int, int, int, int]:
    dirs = []
    for direction in range(0, 450, 90):
        print(direction)
        dirs.append(direction)
    return dirs


directions: list[int, int, int, int] = set_directions()


def get_direction(dirs: list[int, int, int, int]) -> int:
    if check_margins():
        return -180
    return random.choice(dirs)


def on_change_direction() -> None:
    timmy.right(get_direction(directions))


def on_exit_screen() -> None:
    screen.bye()


def on_pause() -> None:
    screen.exitonclick()


def check_margins() -> bool:
    screen_size = screen.screensize()
    timmy_pos = timmy.pos()
    return timmy_pos[0] > screen_size[0] or timmy_pos[0] < 0 \
        or timmy_pos[1] < 0 or timmy_pos[1] > screen_size[1]


timmy: Turtle = Turtle()
timmy.shape("circle")
timmy.resizemode("user")
timmy.shapesize(.1, .1, .2)

colormode(255)
screen: Screen = Screen()
screen.title("Timmy Random Move")
screen.listen()
screen.onkey(on_change_direction, "space")
screen.onkey(on_exit_screen, 'x')
screen.onkey(on_pause, 'p')

while True:
    timmy.pencolor(get_color())
    timmy.speed(random.randint(3, 10))
    timmy.fd(10)
    timmy.left(get_direction(directions))
