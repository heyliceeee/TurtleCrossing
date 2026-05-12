from turtle import Turtle
STARTING_POSITION = (0, -280)
"""
starting position of the turtle
"""
MOVE_DISTANCE = 10
"""
number of the steps that turtle move 
"""
FINISH_LINE_Y = 280
"""
y coordinate of the finish line
"""


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("turtle") # shape
        self.penup()  # no draw while move
        self.setheading(90)
        self.go_to_start()
    def up(self):
        """
        move the player up
        """
        self.forward(MOVE_DISTANCE)
    def is_at_finish_line(self):
        """
        verify if the player is at the finish line
        """
        return self.ycor() > FINISH_LINE_Y
    def go_to_start(self):
        """
        Move the player back to the starting position.
        """
        self.goto(STARTING_POSITION)