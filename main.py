import turtle
from econgrapher import Axes, Line, Tags

# Initialize the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

axes = Axes()
demand = Line((-160, 160), (140, -160))
demand1 = Line((-140, 160), (160, -160))
supply = Line((-160, -160), (160, 160))
tag = Tags(axes, "0", (0, 0))

elements = [axes, demand, demand1, supply, tag]
for e in elements:
    e.render(t)

# Keep the window open until clicked
screen.exitonclick()
