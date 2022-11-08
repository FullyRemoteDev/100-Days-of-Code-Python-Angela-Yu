from turtle import Turtle, Screen

eas_turtle = Turtle()
screen = Screen()


def move_forwards():
    eas_turtle.forward(10)


def move_backwards():
    eas_turtle.backward(10)


def move_counter_clockwise():
    heading_value = eas_turtle.heading() + 10
    eas_turtle.setheading(heading_value)


def move_clockwise():
    heading_value = eas_turtle.heading() - 10
    eas_turtle.setheading(heading_value)


def clear_screen():
    eas_turtle.clear()
    eas_turtle.penup()
    eas_turtle.home()
    eas_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
