from turtle import Turtle, Screen
from random import randint

turtle_obj = Turtle()
screen_obj = Screen()
turtle_obj.shape("circle")

# turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)
# turtle_obj.left(90)
# turtle_obj.forward(100)
# turtle_obj.left(90)

# for i in range (15):
#     turtle_obj.forward(10)
#     turtle_obj.penup()
#     turtle_obj.forward(10)
#     turtle_obj.pendown()

colors = [
    "deep pink",
    "dark violet",
    "indigo",
    "deep sky blue",
    "steel blue",
    "lime",
    "maroon",
]

# for i in range (3, 11):
#     turtle_obj.color(colors[randint(0,6)])
#     angle = 360/i
#     for j in range (0, i):
#         turtle_obj.forward(100)
#         turtle_obj.right(angle)


screen_obj.exitonclick()
