from turtle import Turtle


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.back(10)

    def restart(self):
        self.goto(0, -280)
