from turtle import Turtle, Screen
from random import randint, choice

# Draw a spirograph

turtle05 = Turtle()
screen = Screen()
screen.colormode(255)

no_of_circles = 100

for i in range(no_of_circles):
    turtle05.speed("fastest")
    turtle05.pensize(1)
    turtle05.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    circle_tilt = int(360 / no_of_circles) * i
    turtle05.setheading(circle_tilt)
    turtle05.circle(100)


screen.exitonclick()
