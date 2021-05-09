from turtle import Turtle

WIDTH = 5
HEIGHT = 1
X_POS = 350
Y_POS = 0


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color(color)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
