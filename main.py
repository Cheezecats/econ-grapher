import turtle
from econgrapher import Label, Line

# Initialize the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

label = Label("Hello Turtle!", (0, 0))
label.render(t)

line = Line((-30, -30), (30, 30))
line.render(t)

# Keep the window open until clicked
screen.exitonclick()
