import turtle as t
from random import randint

turtle_obj = t.Turtle()
screen_obj = t.Screen()
t.colormode(255)


def randomColor():
    redLevel = randint(0, 255)
    greenLevel = randint(0, 255)
    blueLevel = randint(0, 255)
    rgb = (redLevel, greenLevel, blueLevel)  # this is a tuple
    return rgb


turtle_obj.speed("fastest")


def draw_spirogrraph(gapSize):
    for i in range(int(360 / gapSize)):
        headedNow = turtle_obj.heading()
        turtle_obj.setheading(headedNow + gapSize)
        turtle_obj.color(randomColor())
        turtle_obj.circle(50)


draw_spirogrraph(5)

screen_obj.exitonclick()
