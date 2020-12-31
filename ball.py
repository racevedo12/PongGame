from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.theMoveSpeed = 0.04

    def move(self):
        theX = self.xcor() + self.xMove
        theY = self.ycor() + self.yMove
        self.goto(theX, theY)

    def bounceWall(self):
        self.yMove *= -1

    def bouncePaddle(self):
        self.xMove *= -1
        self.theMoveSpeed *= 0.9

    def resetPosition(self):
        self.goto(0, 0)
        self.theMoveSpeed = 0.04
        self.bouncePaddle()
