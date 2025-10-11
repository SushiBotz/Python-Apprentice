"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

... # Your code here
tina.pendown()
tina.forward(35)
tina.left(45)
tina.forward(35)
tina.left(90)
tina.forward(35)
tina.left(45)
tina.forward(35)
tina.left(90)
tina.forward(50)

turtle.exitonclick()                    # Close the window when we click on it