from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.speed()
        self.Y_MOVE = 10
        self.X_MOVE = 10

    def move(self):
        new_y =self.ycor() + self.Y_MOVE
        new_x = self.xcor() + self.X_MOVE
        self.penup()
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.Y_MOVE *= -1

    def bounce_x(self):
        self.X_MOVE *= -1

    def refresh(self):
        self.penup()
        self.goto(0, 0)
