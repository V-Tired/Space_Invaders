from turtle import Turtle, Screen
screen = Screen()

"""A class that handles the player object of the game. The required image type is .gif."""


class Player(Turtle):
    """Initialize the player object and set its start position."""
    def __init__(self):
        super().__init__()
        screen.register_shape("ship1.gif")
        self.shape("ship1.gif")
        self.speed("fastest")
        self.penup()
        self.goto((0, -200))
        self.color("DarkSeaGreen3")

    def move(self):
        """Control the player movement via keystrokes contained within the parameters of the screen."""
        def right():
            if self.xcor() < 290:
                self.goto(self.xcor() + 20, (self.ycor()))

        def left():
            if self.xcor() > -290:
                self.goto(self.xcor() - 20, (self.ycor()))
        screen.listen()
        screen.onkey(key="a", fun=left)
        screen.onkey(key="d", fun=right)
