from turtle import Turtle

MOVE_DISTANCE: int = 20
STARTING_POSITIONS: list(tuple[int, int]) = [(0, 0), (-20, 0), (-40, 0)]
RIGHT: int = 0
UP: int = 90
LEFT: int = 180
DOWN: int = 270


def create_turtle_segment() -> Turtle:
    segment: Turtle = Turtle("square")
    segment.pu()
    segment.color("white")

    return segment


class Snake:
    snake: list[Turtle] = []

    def __init__(self):
        self._create_snake()

    """
        Creates a snake by adding turtle segments to the snake list.

        Parameters:
        - self: The SnakeGame object.

        Returns:
        - None

        Description:
        - This function creates a snake by adding three turtle segments to the snake list.
        - Each segment is positioned at a specific coordinate on the screen.
        - The turtle segment is then made visible and added to the snake list.
        - The color of the first segment is set to red for development purposes.
        """

    def _create_snake(self) -> None:
        for pos in STARTING_POSITIONS:
            segment: Turtle = create_turtle_segment()
            segment.goto(pos)
            segment.st()
            self.snake.append(segment)
        self.head = self.snake[0]
        self.head.color("red")  # dev

    """
        Moves the snake forward by one segment.

        This method is responsible for moving the snake forward by one segment. It updates the position of each segment
        of the snake by copying the position of the previous segment. The head of the snake moves forward by a fixed
        distance defined by the constant MOVE_DISTANCE.

        Parameters:
        - self: The Snake object.

        Returns:
        - None

        Example:
        snake = Snake()
        snake.move()
        """

    def move(self) -> None:
        for i in range(len(self.snake) - 1, 0, -1):
            segment_x_pos = self.snake[i - 1].xcor()
            segment_y_pos = self.snake[i - 1].ycor()
            self.snake[i].goto(segment_x_pos, segment_y_pos)
        self.head.forward(MOVE_DISTANCE)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
