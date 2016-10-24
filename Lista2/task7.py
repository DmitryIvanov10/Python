# Lesson2, Task4
# check the method id()

# id() method for integers
x = 2
y = x
print (x, y, id(x), id(y), id(2), id(3))
print ()
y = 3
print (x, y, id(x), id(y))
print ()

# python variables are references to the objects, but not objects itself
# when y=x - y becomes a number from the reference to number 2
# when y=3 - y becomes a number from the reference to number 3, 
# it doesn't affect x, since it is still a number fromt the reference to a number 2

# id() method for lists
x = [1,2]
y = x
print(x, y, id(x), id(y), id([1,2]), id([1,3]))
print ()
y[1] = 3
print(x, y, id(x), id(y))

# python lists are objects, so when y=x - y not only has a value of x,
# but also the same reference is to x and y. 
# When changing y we also change the value from a reference to y,
# which is also a reference to x. So we change x value as well.