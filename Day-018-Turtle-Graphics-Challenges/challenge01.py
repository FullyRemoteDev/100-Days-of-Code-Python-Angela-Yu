from turtle import Turtle, Screen

turtle01 = Turtle()


# Draw a square
for i in range(4):
    turtle01.right(90)
    turtle01.forward(100)

screen = Screen()
screen.exitonclick()
