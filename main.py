from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

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
scoreboard = Scoreboard()

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce()

    # detect ball collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.bounce_paddle()

    # detect collision with left and right wall (paddle miss)
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
