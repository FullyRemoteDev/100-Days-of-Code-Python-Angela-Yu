from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

user_choice = screen.textinput(title="Pick your tutle", prompt="Which turtle will win the race? Enter a colour: ")

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()

            if winning_colour == user_choice:
                print(f"You won! The {winning_colour} colour turtle finished first.")
            else:
                print(f"You Lost! The {winning_colour} colour turtle finished first.")

        randon_distance = random.randint(0, 10)
        turtle.forward(randon_distance)


screen.exitonclick()
