import turtle
from turtle import Turtle, Screen
from random import randint

color_turtle = ["red", "blue", "purple", "green", "yellow", "orange"]

screen = Screen()
screen.setup(width= 500 , height= 400)
y_position = -200
x_position = -230
mult_turtle = []
start_turtle = 0

user_type = turtle.textinput(title = "Make your bet", prompt="Which turtle you won the race? Enter a color: ")

def create_turtles( color, position):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=position)
    mult_turtle.append(new_turtle)

def start_race (index, move):
    mult_turtle[index].fd(move)
    if mult_turtle[index].xcor() > 230:
        if mult_turtle[index].pencolor() == user_type:
            # result = f"You won, the turtle winner is {mult_turtle[index].pencolor()}"
            turtle.title ( f'the turtle winner is {mult_turtle[index].pencolor()}, You won')
        else:
            # result = f"You lost, the turtle winner is {mult_turtle[index].pencolor()}"
            turtle.title ( f'the turtle winner is {mult_turtle[index].pencolor()}, You lost')
        return False
    return True

for colour in color_turtle:
    y_position += 50
    create_turtles(color=colour, position=y_position)

if user_type:
    game = True

while game:
    start_turtle = randint(0, 5)
    move = randint(0,10)
    game = start_race(start_turtle,move)

screen.exitonclick()
