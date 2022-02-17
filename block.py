from turtle import Turtle
import random
colors = [ "red", "blue", "green", "yellow", "purple", "orange", "violet", "white"]
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.shape("square")
        self.penup()
        self.goto(random.randint(300, 340), random.randint(-280, 280))

    def move(self):
        self.forward(-5)