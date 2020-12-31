from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

theScreen = Screen()
theScreen.bgcolor("black")
theScreen.setup(width=800, height=600)
theScreen.title("Pong Game")
theScreen.tracer(0)

paddleRight = Paddle((350, 0))
paddleLeft = Paddle((-350, 0))
theBall = Ball()

theScore = Scoreboard()

theScreen.listen()
theScreen.onkeypress(paddleRight.goUp, "Up")
theScreen.onkeypress(paddleRight.goDown, "Down")
theScreen.onkeypress(paddleLeft.goUp, "w")
theScreen.onkeypress(paddleLeft.goDown, "s")


keepGoing = True
while keepGoing:
    time.sleep(theBall.theMoveSpeed)
    theScreen.update()
    theBall.move()

    # Detecting collisions with the walls
    if theBall.ycor() > 280 or theBall.ycor() < -280:
        theBall.bounceWall()

    # Detect collisions with paddles
    if theBall.distance(paddleRight) < 50 and theBall.xcor() > 340 or theBall.distance(paddleLeft) < 50 and theBall.xcor() < -340:
        theBall.bouncePaddle()

    # Detect Right Paddle miss
    if theBall.xcor() > 380:
        theBall.resetPosition()
        theScore.leftPoint()

    # Detect Left Paddle miss
    if theBall.xcor() < -380:
        theBall.resetPosition()
        theScore.rightPoint()

theScreen.exitonclick()
