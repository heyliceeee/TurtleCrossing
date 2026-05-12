from turtle import Turtle
ALIGN = "left"
"""
alignment of scoreboard
"""
FONT = ("Courier", 24, "normal")
"""
font of scoreboard
"""


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()  # no draw while move
        self.goto(-290, 270) # text up the screen
        self.hideturtle()
        self.update()


    def game_over(self):
        """
        show game over text
        """
        self.clear() # clear the previous level
        self.write(f"GAME OVER! Level: {self.level}", False, align=ALIGN, font=FONT)
        self.hideturtle()
    def update(self):
        """
        update the scoreboard
        """
        self.write(f"Level: {self.level}", False, align=ALIGN, font=FONT)
    def increase_level(self):
        """
        increase score
        """
        self.level += 1
        self.clear() # clear the previous level
        self.update()