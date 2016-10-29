# Lesson4, Task2 and Task3

# But actually min is already built-in function for that

# Find smaller number
def getMinFrom2(a,b):
    if a<b:
        return a
    else:
        return b

# Example
a = 10
b = 7.1 
print ("Smaller number between %2f and %2f is %2f." % (a, b, getMinFrom2(a,b)))
print ()

def getMin(*args):
	minNumber = args[0]
	for number in args:
		minNumber = getMinFrom2(minNumber, number)
	return minNumber
	
# Example
print ("The smallest number in the list is %2f." % getMin(1, 4, -2, 5.1, 10, -3.6, -3.7, -100))