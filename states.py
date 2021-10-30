from turtle import Turtle
class States(Turtle):

    def __init__(self, states, coords):
        super().__init__()
        self.penup()
        self.goto(coords)
        self.write(states)
        self.hideturtle()
