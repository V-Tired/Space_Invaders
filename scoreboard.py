from turtle import Turtle
import os
ALIGN = "center"
FONT = ("Courier", 14, "bold")


"""A class that handles the scoreboard display and the high score text document."""


class Scoreboard(Turtle):
    """Initialize the scoreboard element. Create a text document if there is none to track high score between games."""
    def __init__(self):
        super().__init__()
        if not os.path.exists("high_score.txt"):
            with open(file="high_score.txt", mode="w") as file:
                file.write("0")
        with open(file="high_score.txt", mode="r") as file:
            high_score = int(file.read())
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

    def new_high_score(self):
        """Update the high score file with new high score."""
        with open(file="high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def update(self):
        """Moves scoreboard into position and displays info."""
        self.clear()
        self.goto(200, 200)
        self.write(arg=f"Score: {self.score} \nHigh Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        """Add points to score."""
        self.score += 100
        self.update()

    def redo(self):
        """Update the high score at end of game, reset score to zero."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = 0
        self.update()
