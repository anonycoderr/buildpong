from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# creating left and right paddles
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "q")
screen.onkey(paddle_l.move_down, "d")



game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    # detect collision with top and bottom walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    #detect collision with paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #right paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        ball.bounce_x()
        scoreboard.r_point()














screen.exitonclick()
