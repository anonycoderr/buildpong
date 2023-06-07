from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):

        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.goto(position)
        self.score = 0

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

