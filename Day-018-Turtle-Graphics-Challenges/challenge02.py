from turtle import Turtle, Screen

turtle02 = Turtle()


# Draw a dashed line
for _ in range(20):
    turtle02.forward(10)
    turtle02.penup()
    turtle02.forward(10)
    turtle02.pendown()

screen = Screen()
screen.exitonclick()
