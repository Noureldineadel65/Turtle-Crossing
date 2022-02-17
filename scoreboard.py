from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(-205, (0.83 * (600 / 2)))
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=('Courier', 20, 'italic'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=('Courier', 25, 'bold'))