from turtle import Turtle, Screen
import time

screen = Screen()
BULLET_SPEED = 20

"""A class that handles the bullet objects of the game."""

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullets = []

    def shoot(self, position):
        """Create bullet objects if there are less than 5 on screen. Send them to the position of the player."""
        def create_bullet():
            if len(self.bullets) < 5:
                bullet = Turtle()
                bullet.shape = "circle"
                bullet.speed("fastest")
                bullet.shapesize(.5)
                bullet.penup()
                bullet.setheading(90)
                bullet.goto(position)
                bullet.color("DodgerBlue")
                self.bullets.append(bullet)


        screen.listen()
        screen.onkey(key="space", fun=create_bullet)

    def bullet_move(self):
        """Move the bullets a certain distance every loop if they have not reached the edge of the screen."""
        for each in self.bullets:
            if each.ycor() < 260:
                each.forward(BULLET_SPEED)
            else:
                self.bullets.remove(each)
                each.hideturtle()
