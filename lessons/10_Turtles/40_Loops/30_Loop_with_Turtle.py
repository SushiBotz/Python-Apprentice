"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

... # Your code here

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()   
               # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(5)               # Make the turtle move as fast, but not too fast. 

for i in range(5):   
    print('Loop iteration', i)   
    tina.forward(150)                       # Move tina forward by the forward distance
    tina.left(72)                  # Turn tina left by the left turn
turtle.exitonclick()                    # Close the window when we click on i