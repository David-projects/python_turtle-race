import random
from turtle import Turtle, Screen
from random import choice
from turtle_racer import TurtleRacer

screen = Screen()
screen.setup(width=500, height=400)

# setup racers
players = int(screen.numinput(title="Number of racers", prompt="Enter the number of racers"))
user_colour = screen.textinput(title="make your bet", prompt="Which turtle will win? Enter your colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
colours.remove(user_colour)
y = -70
all_racers = []

for turtle_index in range(0, players):
    if turtle_index == 0:
        new_turtle = TurtleRacer(Turtle(shape="turtle"),user_colour)
    else:
        new_turtle = TurtleRacer(Turtle(shape="turtle"),choice(colours))

    new_turtle.penup()
    new_turtle.goto_start(x=-230, y=y)
    all_racers.append(new_turtle)
    y += 40

if user_colour:
    start_race = True

while start_race:
    for racer in all_racers:
        if racer.start_race():
            if racer.get_colour() == user_colour:
                print("You win")
            else:
                print(f"You lose: {racer.get_colour()} was the winner")
            start_race = False
            break


screen.exitonclick()