# Lesson2, Task1

# create tuple
myTuple = (0, 1, 2, 3, 4, "five", "six", "seven", "eight", "nine")
 

# print first Three 
print ("First three elements: ", end = '')
print (myTuple[:3])
print ()

# print last two 
print ("Last two elements: ", end = '')
print (myTuple[(len(myTuple)-2):])
print ()

# print each second starting with second 
print ("Each second element starting with second: ", end = '')
print (myTuple[2::2])
print ()

# length of the tuple
print ("Length of the tuple: %i" % len(myTuple))
print ()

# length of the prelast element 
print ("Length of the prelast element: %i" % len(myTuple[len(myTuple) - 2]))
print ()

# concatenate parts of the tuple and print
print (myTuple[:5] + (5, 6) + myTuple[-3:])
print ()
# print parts of the tuple one by one
print (myTuple[:5], (5, 6), myTuple[-3:])
print ()

# add an element to the tuple and print the tuple
newElement = ""
l = list(myTuple)
l.append(newElement)
myTuple = tuple(l)

for i in range(len(myTuple)): 
    print (myTuple[i], end=" ")

print ()