from turtle import Turtle, Screen
from random import randint, choice

# Generate a random walk

turtle04 = Turtle()
screen = Screen()
screen.colormode(255)

for _ in range(100):
    turtle04.speed("fast")
    turtle04.pensize(5)
    turtle04.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    random_direction = [0, 90, 180, 270]
    turtle04.setheading(choice(random_direction))
    turtle04.forward(25)


screen.exitonclick()
