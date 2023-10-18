from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


score = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()






screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if (ball.distance(r_paddle) < 60 and ball.xcor() >320) or (ball.distance(l_paddle) < 60 and  ball.xcor() < -320 ):
        ball.paddle_bounce()
        ball.faster()

        
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()
    
    if ball.xcor() > 400:
        score.count_left()
        ball.reset_position()
        

    if ball.xcor() < -400:
        score.count_right()
        ball.reset_position()
        




screen.exitonclick()
