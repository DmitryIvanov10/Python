# Lesson3, Task6
""" I didn't find the compiler which would work with 
both Python3 functions (such as division, input and eval) 
and turtle, but the code should work.
It is written with assumption, that division '/' would give float number
and eval would work for input."""

import turtle

# Create a turtle to draw
turtle = turtle.Turtle()

# Get the polygon properties and amount of polygons to draw from the user
n_sides = eval(input("Give the amount of sides of the polygon: "))
length = eval(input("Give the length of the side of the polygon: "))
n_polygons = eval(input("Give the amount of polygons: "))

# Scaling, so the final picture would be the same size for different side amounts
length = length * (10 / n_sides)

# The speed of a turtle
turtle.speed(20)

# Function to draw one polygon of N sides and the length of a side L
def drawPolygon(N, L):
	for i in range(N):
		turtle.forward(L)
		turtle.right(360/N)
		
# Function to draw A polygons in a circle
def drawPolygons(N, L, A):
	for j in range(A):
		drawPolygon(N, L)
		turtle.right(360/A)

# Draw the figure
drawPolygons(n_sides, length, n_polygons)

# Leave the window with the figure opened
turtle.mainloop()