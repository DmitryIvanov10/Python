<<<<<<< HEAD
# Lesson4, Task5

# Get coefficients of quadratic equation from user
print ("Please, give the coefficients of the quadratic equation.") 
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

# Calculate delta
delta = b**2 - 4*a*c

# Calculate and print solutions
if delta > 0:
    print ("You have 2 rational solutions.")
    x1 = (-b + delta**(0.5))/(2*a)
    x2 = (-b - delta**(0.5))/(2*a)
    print ("X1 = %2f" % x1)
    print ("X2 = %2f" % x2)
elif delta == 0:
    print ("You have 1 rational solution.")
    x1 = -b / (2*a)
    x2 = x1
    print ("X = %2f" % x1)
else:
    print ("You have 2 complex solutions.")
    delta *= -1
    xRe = -b / (2*a)
    xIm = delta**(0.5) / (2*a)
    x1 = xRe + xIm*1j
    x2 = xRe - xIm*1j
    print ("X1 = %2f + %2fi" % (xRe, xIm))
=======
# Lesson4, Task5

# Get coefficients of quadratic equation from user
print ("Please, give the coefficients of the quadratic equation.") 
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

# Calculate delta
delta = b**2 - 4*a*c

# Calculate and print solutions
if delta > 0:
    print ("You have 2 rational solutions.")
    x1 = (-b + delta**(0.5))/(2*a)
    x2 = (-b - delta**(0.5))/(2*a)
    print ("X1 = %2f" % x1)
    print ("X2 = %2f" % x2)
elif delta == 0:
    print ("You have 1 rational solution.")
    x1 = -b / (2*a)
    x2 = x1
    print ("X = %2f" % x1)
else:
    print ("You have 2 complex solutions.")
    delta *= -1
    xRe = -b / (2*a)
    xIm = delta**(0.5) / (2*a)
    x1 = xRe + xIm*1j
    x2 = xRe - xIm*1j
    print ("X1 = %2f + %2fi" % (xRe, xIm))
>>>>>>> 0b1190fafe0f850c1325c7e615b1abd120588142
    print ("X2 = %2f - %2fi" % (xRe, xIm))