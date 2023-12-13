from turtle import Screen, Turtle
from trap import Trap
from ball_pong import Ball_pong
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("midnight blue")
screen.title("Welcome to the Ping pong game!")
screen.tracer(0)

r_trap = Trap((360, 0))
l_trap = Trap((-360, 0))
ball_pong = Ball_pong()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_trap.go_up, "Up")
screen.onkey(r_trap.go_down, "Down")
screen.onkey(l_trap.go_up, "w")
screen.onkey(l_trap.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball_pong.move()

    if ball_pong.ycor() > 280 or ball_pong.ycor() < -280:
        ball_pong.jump_y()

    if ball_pong.distance(r_trap) < 50 and ball_pong.xcor() > 330 or ball_pong.distance(
            l_trap) < 50 and ball_pong.xcor() < -330:
        ball_pong.jump_x()

    if ball_pong.xcor() > 380:
        ball_pong.reset_position()
        scoreboard.l_point()

    if ball_pong.xcor() < -380:
        ball_pong.reset_position()
        scoreboard.r_point()

screen.exitonclick()
