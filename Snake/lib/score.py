from turtle import Turtle


class Score(Turtle):
    score_val: int

    def __init__(self):
        super(Score, self).__init__()
        self.score_val = -1
        self.hideturtle()
        self.color("grey")
        self.add_score()

    def add_score(self):
        self.score_val += 1
        self.clear()
        self.write(f"Score: {self.score_val}", False, align="center", font=("Arial", 24, "normal"))
