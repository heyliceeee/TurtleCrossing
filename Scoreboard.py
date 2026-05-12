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
        self.level = 1
        self.hideturtle()
        self.penup()  # no draw while move
        self.goto(-290, 270) # text up the screen
        self.update()


    def game_over(self):
        """
        show game over text
        """
        self.clear() # clear the previous level
        self.write(f"GAME OVER! Level: {self.level}", False, align=ALIGN, font=FONT)
    def update(self):
        """
        update the scoreboard
        """
        self.clear()
        self.write(f"Level: {self.level}", False, align=ALIGN, font=FONT)
    def increase_level(self):
        """
        increase score
        """
        self.level += 1
        self.update()