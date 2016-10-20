# Lesson1, Task5

import sys
import math

# function to calculate float as a fraction
from fractions import Fraction 

# variable to calculate the fraction
x = 2.2

#print results
print ("Results for the number %2f :" % x)
print ()
print ("Without limit on denominator")
print (Fraction(x))
print ()
print ("With limit on denominator")
print (Fraction(x).limit_denominator())
print ()
print ("Fraction from irrational number (Pi)")
print (Fraction(math.pi))
print ()

# check the system info about float numbers
x = sys.float_info.max

# print the result
print ("Max floating point number: " + str(x))
print ("The number bigger than Max: %2f" % (2 * x))