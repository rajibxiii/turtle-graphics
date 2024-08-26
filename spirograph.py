import turtle as t
from random import randint

turtle_obj = t.Turtle()
screen_obj = t.Screen()
t.colormode(255)

def randomColor ():
    redLevel = randint (0, 255)
    greenLevel = randint (0, 255)
    blueLevel = randint (0, 255)
    rgb  = (redLevel, greenLevel, blueLevel) # this is a tuple
    return rgb

# for i in range (300):
#     # choiceDir = randint(0, 3)
#     choiceAngle = angles[randint(0, 3)]
#     turtle_obj.color(randomColor())
#     turtle_obj.speed("fastest")

#     turtle_obj.forward(20)
#     turtle_obj.setheading(angles[randint(0, 3)])

turtle_obj.speed("fastest")
turtle_obj.color(randomColor())
turtle_obj.circle(50)