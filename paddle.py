from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.position = position
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def goUp(self):
        theNewY = self.ycor() + 30
        self.goto(self.xcor(), theNewY)

    def goDown(self):
        theNewY = self.ycor() - 30
        self.goto(self.xcor(), theNewY)