from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# TODO create the GUI from multiple components:
#  break down the components into separate classes
#  two paddles consisting of two turtles
#  one ball consisting of one turtle
#  one scoreboard with a net

# TODO create paddle and make it onkey movable

# TODO create the ball and make it movable

# TODO detect ball collision with wall and make it bounce

# TODO detect collision with paddle and make the ball bounce back

# TODO detect collision with left and right wall (paddle miss)

# TODO create the scoreboard and keep score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)  # animation off

l_paddle = Paddle(xcor=-380)
r_paddle = Paddle(xcor=380)

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
