# Lesson8, Task5

# import from modules
from itertools import groupby

# create look and say sequence
def look_and_say(a1, n):
    """Creates a list of elements of the sequence look_and_say 
    where a1 is a first element, and n is amount of elements in the sequence"""
    
    # make a list of digits from number
    a1 = str(a1)
    bufer = []
    for i in range(len(a1)):
        bufer.append(eval(a1[i]))
    a1 = bufer
    
    # create list to save all elements of th sequence
    result = [a1]

    # fill result list with all n elements one by one
    for i in range(n):
        a_next = []
        for number,amount in groupby(list(a1)):
            a_next += [len(list(amount))]
            a_next += [number]
        a1 = a_next
        result += [a_next]

    return result

# initial data about the first element of the sequence and amount of elements
a1 = 1
n = 10

# generate list of the elements of the sequence
my_list = look_and_say(a1, n)

# print results
print ("Look-and-Say sequence:")
print ()
for j in range(n):
    print ("a{}: ".format(j+1), end = '')
    print (*my_list[j])