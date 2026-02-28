"""Demonstrates the effect of tax on the consumer side - demand curve shifts inward (left)."""

import turtle
from econgrapher import Axes, Line, Label, Tags

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Draw axes
axes = Axes("Q", "P", ("Times New Roman", 24, "italic"))
axes.render(t)

# Supply curve (upward sloping)
supply = Line((-150, -150), (150, 150), "solid")
supply.render(t)
Label("S", (160, 150)).render(t)

# Original demand curve (downward sloping)
demand1 = Line((-100, 150), (150, -100), "solid")
demand1.render(t)
Label("D₁", (155, -100)).render(t)

# New demand curve after tax (shifted left/inward)
demand2 = Line((-150, 100), (100, -150), "solid")
demand2.render(t)
Label("D₂", (105, -150)).render(t)

# Mark original equilibrium (intersection of S and D1)
# S: y = x, D1: y = -x + 50, so x = 25, y = 25
tags1 = Tags(axes, "1", (25, 25))
tags1.render(t)

# Mark new equilibrium after tax (intersection of S and D2)
# S: y = x, D2: y = -x - 25, so x = -12.5, y = -12.5
# But for visual purposes, let's use a reasonable point
tags2 = Tags(axes, "2", (-20, -20))
tags2.render(t)

# Arrow indicating shift direction
Label("← Tax shifts demand", (-50, 130)).render(t)

# Keep the window open until clicked
screen.exitonclick()
