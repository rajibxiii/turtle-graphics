import turtle as t
from random import randint

turtle_obj = t.Turtle()
screen_obj = t.Screen()
turtle_obj.shape("circle")
turtle_obj.shapesize(0.5, 0.5, 0.5)
turtle_obj.pensize(10)
t.colormode(255)

# colors = [
#     "deep pink",
#     "dark violet",
#     "indigo",
#     "deep sky blue",
#     "steel blue",
#     "lime",
#     "maroon",
# ]

def randomColor ():
    redLevel = randint (0, 255)
    greenLevel = randint (0, 255)
    blueLevel = randint (0, 255)
    rgb  = (redLevel, greenLevel, blueLevel) # this is a tuple
    return rgb

angles = [0, 90, 180, 270]

for i in range (300):
    # choiceDir = randint(0, 3)
    choiceAngle = angles[randint(0, 3)]
    turtle_obj.color(randomColor())
    turtle_obj.speed("fastest")

    # if choiceDir == 0:
    #     turtle_obj.forward(20)
    # elif choiceDir == 1:
    #     turtle_obj.right(choiceAngle)
    #     turtle_obj.forward(20)
    # elif choiceDir == 2:
    #     turtle_obj.left (choiceAngle)
    #     turtle_obj.forward(20)
    # else:
    #     turtle_obj.backward(20)

    turtle_obj.forward(20)
    turtle_obj.setheading(angles[randint(0, 3)])
