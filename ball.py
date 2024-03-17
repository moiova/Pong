from turtle import Turtle

# create the ball and make it movable
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.x_move = 10
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9 # increase ball speed

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle() # reverse ball start direction

    def increase_speed(self):
        current_speed = self.speed()
        self.speed(current_speed + 1)