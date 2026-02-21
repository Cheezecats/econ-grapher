import turtle

# Initialize the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Position the turtle
t.penup()
t.goto(0, 0)
t.pendown()

# Write text with a designated font
text_content = "Rendered with Turtle"
font_configuration = ("Helvetica", 24, "bold")

t.write(text_content, align="center", font=font_configuration)

# Keep the window open until clicked
screen.exitonclick()
