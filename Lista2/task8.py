# Lesson2, Task4

x = (a, b, c) = (1, 2, 3)
print ("x type is %s" % type(x))
print ("x = ", end = "")
print (x)
print ("a = %i" % a)
print ("b = %i" % b)
print ("c = %i" % c)
print ()

x = a, b, c = 1, 2, 3
print ("x type is %s" % type(x))
print ("x = ", end = "")
print (x)
print ("a = %i" % a)
print ("b = %i" % b)
print ("c = %i" % c)
print ()

x = [a, b, c] = [1, 2, 3]
print ("x type is %s" % type(x))
print ("x = ", end = "")
print (x)
print ("a = %i" % a)
print ("b = %i" % b)
print ("c = %i" % c)
print ()

a = 1
b = "one"

a,b = b,a
print ("a = %s" % a)
print ("b = %i" % b)