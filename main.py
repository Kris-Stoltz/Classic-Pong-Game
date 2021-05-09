from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import winsound
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0), 'blue')
r_paddle = Paddle((350, 0), 'red')
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        winsound.PlaySound('Wall.wav', winsound.SND_ASYNC)

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        winsound.PlaySound('Paddle.wav', winsound.SND_ASYNC)

    # detect if right paddle misses
    if ball.xcor() > 380:
        winsound.PlaySound('Out.wav', winsound.SND_ASYNC)
        ball.reset_position()
        scoreboard.l_point()
        screen.update()
        time.sleep(0.5)

    # detect if left paddle misses
    if ball.xcor() < -380:
        winsound.PlaySound('Out.wav', winsound.SND_ASYNC)
        ball.reset_position()
        scoreboard.r_point()
        screen.update()
        time.sleep(0.5)


screen.exitonclick()
