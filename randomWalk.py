from turtle import Turtle, Screen
from random import randint

turtle_obj = Turtle()
screen_obj = Screen()
turtle_obj.shape("circle")
turtle_obj.shapesize(0.5, 0.5, 0.5)
turtle_obj.pensize(10)

colors = [
    "deep pink",
    "dark violet",
    "indigo",
    "deep sky blue",
    "steel blue",
    "lime",
    "maroon",
]
angles = [0, 90, 180, 270]

for i in range (300):
    choiceDir = randint(0, 3)
    choiceAngle = angles[randint(0, 3)]
    turtle_obj.color(colors[randint(0,6)])
    turtle_obj.speed(10)
    if choiceDir == 0:
        turtle_obj.forward(20)
    elif choiceDir == 1:
        turtle_obj.right(choiceAngle)
        turtle_obj.forward(20)
    elif choiceDir == 2:
        turtle_obj.left (choiceAngle)
        turtle_obj.forward(20)
    else:
        turtle_obj.backward(20)
