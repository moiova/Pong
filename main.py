from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# TODO create the GUI from multiple components:
#  one scoreboard with a net

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

    # detect collision with wall
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce()

    # detect ball collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330:
        ball.bounce_paddle()

    elif ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_paddle()

    else:
        pass

screen.exitonclick()
