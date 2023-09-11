from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.setpos(self.position)

    def up(self):
        y_cor = self.ycor() + 20
        self.setpos(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.setpos(self.xcor(), y_cor)
