# Lesson1, Task1

import math

# create a list of numbers
arr = [2, 3, 5, -8]

# calculate the sum and the average of the elements
sum = 0
for i in range(len(arr)): 
    sum += arr[i]

average = float(sum) / len(arr)

# print results
print ("Sum of the elements is %i" % sum)
print ("Average is %.2f" % average)

# print results for sin and cos
print ("cos(pi) = %.2f" % math.cos(math.pi))
print ("sin(2*pi/3) = %2f" % math.sin(math.pi * 2 / 3))
print ("sin(2*pi/3 - pi) = %2f" % math.sin(math.pi * 2 / 3 - math.pi))