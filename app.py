from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)
user_bet = screen.textinput(title="HighScore", prompt="What should be the high-score?: ").lower()

paddle = Turtle()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #  Detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect when right paddle misses
    if ball.xcor() > 390:
        ball.reset_post()
        scoreboard.l_point()

    # Detect left sided paddle miss
    if ball.xcor() < -380:
        ball.reset_post()
        scoreboard.r_point()
    #
    # right_player_score = scoreboard.l_point()
    # left_player_score = scoreboard.l_point()
    #
    # if user_bet >= right_player_score:
    #     scoreboard.player_2_win()
    # elif scoreboard.l_point() == user_bet:
    #     scoreboard.player_1_win()
screen.exitonclick()
