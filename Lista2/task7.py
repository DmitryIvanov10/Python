# Lesson2, Task4
# check the method id()

# id() method for integers
x = 2
y = x
print (x, y, id(x), id(y))
print ()
y = 3
print (x, y, id(x), id(y))
print ()

# id() method for lists
x = [1,2]
y = x
print(x, y, id(x), id(y))
print ()
y[1] = 3
print(x, y, id(x), id(y))