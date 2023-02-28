from turtle import Turtle, Screen
from random import choice

color_turtle = ["red", "blue", "purple", "green", "yellow", "orange"]

screen = Screen()
y_position = -200


def create_turtles( color, position):
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-200, y= position)


for colour in color_turtle:
    y_position += 50
    create_turtles(color=colour, position=y_position)

screen.exitonclick()
