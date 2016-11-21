# Lesson5, Task3,4

# function to find next Collatz element 
def next_collatz(number):
    if number%2 == 0:
        return number/2
    else:
        return number*3 + 1

# function to find n-th Collatz element when first element is c0
def n_collatz(c0, n):
    for i in range(1,n):
        c0 = next_collatz(c0)
    return c0

# function to find first appearence of 1 in Collatz series
def collatz_first_one(c0):
    i = 1
    while c0!=1:
        i += 1
        c0 = next_collatz(c0)
    return i

# print results
print ("Give the first element of Collatz series.")
c0 = eval(input("c0 = "))
print ()
print ("What element would You like to know?")
n = eval(input("n = "))
print ()
print ("{} element is equal to {}".format(n, n_collatz(c0, n)))
print ()
print ("First appearence of 1 is {} element".format(collatz_first_one(c0)))