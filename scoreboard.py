from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("Times New Roman", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("Times New Roman", 80, "normal"))

    def leftPoint(self):
        self.leftScore += 1
        self.updateScoreboard()

    def rightPoint(self):
        self.rightScore += 1
        self.updateScoreboard()
