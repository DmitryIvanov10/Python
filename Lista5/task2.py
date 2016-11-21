# Lesson5, Task2

# import own module
import arithmetic_progression

# initial parameters
print ("Give the arithmetic progression parameters")
a1 = eval(input("a1 = "))
r = eval(input("r = "))
n = eval(input("n = "))

# print results
print ("Arithmetic progression parameters:")
print ("a1 = {}, r = {}".format(a1, r))
print ()
print ("a{} = {}".format(n,arithmetic_progression.nth_element(a1,r,n)))
print ("S{} = {}".format(n,arithmetic_progression.n_sum(a1,r,n)))