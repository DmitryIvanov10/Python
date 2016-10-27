# Lesson2, Task3

# create a list using range()
myList = range(3, 100, 3)
myList = list(myList)

# delete elements from list using del
del myList[5::3]

# calculate an average value of the elements and print it
average = sum(myList) / len(myList)
print ("Average value of the elements: %2f" % average)