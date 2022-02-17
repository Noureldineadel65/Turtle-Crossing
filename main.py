
from turtle import Screen
from tortoise import Tortoise
from block import Block
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)
tortoise = Tortoise()
scoreboard = Scoreboard()
game_on = True

screen.listen()
screen.onkey(tortoise.move_forward, "Up")
screen.onkey(tortoise.move_backward, "Down")
blocks = []
SPEED = 0.1
drain_time = 0
while game_on:
    time.sleep(SPEED)
    screen.update()
    drain_time -= 0.1
    if round(drain_time) == 0:
        for i in range(0, 3):
            block = Block()
            blocks.append(block)
        drain_time = 3
    for i in blocks:
        i.move()
        if tortoise.distance(i) < 30:
            scoreboard.game_over()
            game_on = False
        if i.xcor() <= -310:
            done_indx = blocks.index(i)
            del done_indx
    if tortoise.ycor() == 280:
        scoreboard.update_score()
        tortoise.restart()
        SPEED -= 0.01



screen.exitonclick()