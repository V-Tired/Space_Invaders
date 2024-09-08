from turtle import Turtle, Screen
import random
LEFT = 180
RIGHT = 0
DOWN = 270
DOWN_DISTANCE = 30

screen = Screen()

"""A class that handles the enemy objects of the game. The required image type is .gif."""
class Enemy:
    def __init__(self):
        self.enemies = []

    def on_timer(self):
        """Spawn new enemies every 3 seconds if there are less than 5 enemies total."""
        if len(self.enemies) < 5:
            self.spawn(2)
        screen.ontimer(t=3000, fun=self.on_timer)

    def spawn(self, num):
        """Create enemy objects in the upper part of the screen. Append them to enemy list."""
        for each in range(num):
            screen.register_shape("alien1.gif")
            enemy = Turtle(shape="alien1.gif")
            enemy.penup()
            enemy.shapesize(1.5)
            enemy.color("LightPink")
            enemy.pensize(1)
            enemy.speed("fastest")
            my_range = range(-300, 300, 50)
            x = random.choice(my_range)
            y = 200
            enemy.goto(x, y)
            enemy.setheading(180)
            self.enemies.append(enemy)

    def move(self):
        """Move enemies a certain distance every loop between both edges of the screen, then shift down and switch."""
        for enemy in self.enemies:
            enemy.forward(random.randint(7, 10))
            if enemy.xcor() <= -300:
                enemy.setheading(DOWN)
                enemy.forward(DOWN_DISTANCE)
                enemy.setheading(RIGHT)

            elif enemy.xcor() >= 300:
                enemy.setheading(DOWN)
                enemy.forward(DOWN_DISTANCE)
                enemy.setheading(LEFT)
