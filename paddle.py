from turtle import Turtle

UP = 90
DOWN = 270

DISTANCE = 20

# create and move paddle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        super().penup()
        super().shape("square")
        super().color("white")
        super().shapesize(stretch_wid=5, stretch_len=1)
        super().goto(x=380, y=0)

    def up(self):
        new_y = super().ycor() + DISTANCE
        super().goto(super().xcor(), new_y)

    def down(self):
        new_y = super().ycor() - DISTANCE
        super().goto(super().xcor(), new_y)
