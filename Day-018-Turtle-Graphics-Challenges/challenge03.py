from turtle import Turtle, Screen
from random import randint


# Draw different shapes - triangle, square, pentagon, hexagon,
# heptagon, octagon, nonagon,and decagon

turtle03 = Turtle()
screen = Screen()
screen.colormode(255)


def draw_shape(shape_sides):
    angle = 360 / shape_sides
    for i in range(shape_sides):
        turtle03.forward(100)
        turtle03.right(angle)


for shape_sides_number in range(3, 11):
    turtle03.pensize(3)
    turtle03.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    draw_shape(shape_sides_number)

screen.exitonclick()
