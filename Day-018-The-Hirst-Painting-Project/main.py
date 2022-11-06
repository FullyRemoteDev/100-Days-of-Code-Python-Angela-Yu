import turtle as turtle_module
import random

# Colours extracted from image.jpg file using extract_colours.py
# and colorgram package.
# Colours close to white have been removed.
colours_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                (176, 192, 208), (168, 99, 102)]

turtle = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.colormode(255)

# Values for the painting
size_of_dots = 20
number_of_dots = 100
dots_per_row = 10
distance_between_dots = 50

# Change initial position of the turtle
turtle.penup()
turtle.hideturtle()
position = (distance_between_dots * (dots_per_row - 1)) / 2
turtle.setpos(-position, -position)

turtle.speed('fastest')

for dot_count in range(1, number_of_dots + 1):
    dot_colour = random.choice(colours_list)
    turtle.dot(size_of_dots, dot_colour)
    turtle.forward(distance_between_dots)

    if dot_count % dots_per_row == 0:
        turtle.backward(distance_between_dots * dots_per_row)
        turtle.left(90)
        turtle.forward(distance_between_dots)
        turtle.right(90)


screen.exitonclick()
