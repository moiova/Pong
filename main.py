from turtle import Screen, Turtle

# TODO create the GUI from multiple components:
#  break down the components into separate classes
#  two paddles consisting of two turtles build of two segment turtles
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

screen.update()

screen.exitonclick()
