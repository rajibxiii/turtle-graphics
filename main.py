from turtle import Turtle, Screen
from random import randint

turtle_obj = Turtle()
screen_obj = Screen()
turtle_obj.shape("square")

for i in range (15): ## dotted line
    turtle_obj.forward(10)
    turtle_obj.penup()
    turtle_obj.forward(10)
    turtle_obj.pendown()

screen_obj.exitonclick()