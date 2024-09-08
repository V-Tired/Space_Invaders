from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from enemies import Enemy
from bullet import Bullet
import time

"""A knock-off version of space invaders for a class project"""


screen = Screen()
screen.tracer(0)
screen.setup(height=500, width=600)
screen.bgcolor("gray5")
player = Player()
scoreboard = Scoreboard()
enemy = Enemy()
enemy.on_timer()
bullet = Bullet()
bullet.hideturtle()
game = True


def game_over():
    """Create Text on screen to display Game Over"""
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color('white')
    style = ("Courier", 30, "bold")
    turtle.write('Game Over', font=style, align='center')
    turtle.hideturtle()


enemy.spawn(7)
x = .04
while game:
    time.sleep(x)
    enemy.move()
    screen.update()
    player.move()
    bullet.shoot(player.position())
    bullet.bullet_move()
    for each in enemy.enemies:
        if enemy.enemies[0].ycor() <= -180:
            game = False
            break
        for slug in bullet.bullets:
            if each.distance(slug) < 15:
                scoreboard.increase_score()
                each.hideturtle()
                each.goto(900, 0)
                enemy.enemies.remove(each)
                slug.hideturtle()
                slug.goto(0, 301)
                x -= .0004
    if scoreboard.score % 2000 == 0:
        enemy.spawn(10)
        scoreboard.score += 100

    if scoreboard.score % 5000 == 0:
        enemy.spawn(15)
        scoreboard.score += 100

game_over()
scoreboard.redo()
screen.ontimer(t=6000, fun=screen.bye)
screen.exitonclick()
