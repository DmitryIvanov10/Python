# Lesson3, Task1

# Create list of even numbers
even = range(2, 100, 2)

# Define variables
a, b, c, *d = even

# Print variables
print ("a = %i\nb = %i\nc = %i\nd = " % (a,b,c) + str(d))
print ()

# Redefine variables
a, b, c, *_ = even

# Print variables
print ("a = %i\nb = %i\nc = %i\n_ = " % (a,b,c) + str(_))
print ()

# Define other variables
start, *myList, end = even

# Print variables
print ("start = %i\nend = %i\nmyList = " % (start, end) + str(myList))