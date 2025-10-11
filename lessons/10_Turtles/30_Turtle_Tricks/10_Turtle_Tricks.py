"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window


# Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here
tina = turtle.Turtle()   
 
tina.pendown()
tina.forward(45)
tina.left(90)
tina.forward(45)
tina.left(135)
tina.forward(63.6396103068)
turtle.exitonclick()                    # Close the window when we click on it