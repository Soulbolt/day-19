from turtle import Turtle, Screen

ralph = Turtle()
screen = Screen()


def move_forwards():
    ralph.forward(10)


screen.listen() # Listen for a key action, in this case the space bar key
screen.onkey(key="space", fun=move_forwards)  # When calling a function in here, the () is not needed
screen.exitonclick()
