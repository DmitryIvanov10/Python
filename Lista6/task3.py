# Lesson6, Task3

# import data from modules
from sys import argv
from math import cos

# constant for accuracy of calculations
epsilon = 0.05

# obtuse, acute, rectangular

def perimeter(a, b, c):
    """Gets perimeter of a triangle"""
    """a, b, c - sides of a triangle"""
    return a+b+c

def area(a, b, c):
    """Gets area of a triangle"""
    """a, b, c - sides of a triangle"""
    p = perimeter(a, b, c) / 2
    return (p*(p-a)*(p-b)*(p-c))**(1/2)

def side_type(a, b, c):
    """Returns if a triangle is random, isoscale or equilateral"""
    """a, b, c - sides of a triangle"""
    # check if equilateral
    if a==b==c:
        return "equilateral"
    # check if isoscale
    elif a==b or a==c or b==c:
        return "isoscale"
    else:
        return "average"

def angle_type(a, b, c):
    """Returns if a triangle is acute, obtuse or rectangular"""
    """a, b, c - sides of a triangle"""
    # check if rectangular
    if abs(a**2 + b**2 - c**2) < epsilon or \
       abs(a**2 + c**2 - b**2) < epsilon or \
       abs(c**2 + b**2 - a**2) < epsilon:
        return "rectangular"
    # check if obtuse
    elif cos((a**2 + b**2 - c**2)/(2*a*b)) < 0 or \
         cos((a**2 + c**2 - b**2)/(2*a*c)) < 0 or \
         cos((c**2 + b**2 - a**2)/(2*c*b)) < 0:
        return "obtuse"
    else:
        return "acute"

# check if correct amount of arguments
if len(argv) != 4:
    print ("Wrong amount of arguments.")
else:
    # get arguments - sides of the triangle
    a = eval(argv[1])
    b = eval(argv[2])
    c = eval(argv[3])
    print ("Sides are ({}, {}, {})".format(a, b, c))
    # check if the triangle exists
    if a > b+c or b > a+c or c > a+b:
        print ("No triangle with these side lengths.")
    else:
        # print results
        print ("The triangle is {} and {}.".format( \
                side_type(a, b, c), angle_type(a, b, c)))
        print ("P = {}".format(round(perimeter(a, b, c),2)))
        print ("side_type = {}".format(round(area(a, b, c),2)))