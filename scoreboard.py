from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.goto(x=-100, y=200)
        self.write(self.l_score, move=False, align='center', font=('Arial', 48, 'normal'))
        self.goto(x=100, y=200)
        self.write(self.r_score, move=False, align='center', font=('Arial', 48, 'normal'))
