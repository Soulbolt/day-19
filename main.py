from turtle import Turtle, Screen
# Create an Etch_a_sketch app
ralph = Turtle()
screen = Screen()


def move_forwards():
    ralph.forward(10)


def move_backwards():
    ralph.backward(10)


def turn_left():
    new_heading = ralph.heading() + 10
    ralph.setheading(new_heading)


def turn_right():
    new_heading = ralph.heading() - 10
    ralph.setheading(new_heading)


def clear():
    ralph.clear()
    ralph.penup()
    ralph.home()
    ralph.pendown()


screen.listen()  # Listen for a key action
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")  # When calling a function in here, the () is not needed
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
