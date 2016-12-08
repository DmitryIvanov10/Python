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
    result = []
    # add first element to ehe sequence
    result.append(a1)
    
    # calculate other elements of the sequence
    for i in range(1, n):
        # a1 here would be the two dimensional array, where each pair is amount of numbers
        a1 = [(len(list(amount)), number) for number,amount in groupby(list(a1))]
        
        # make one dimensional array to save into the element of the sequence
        k = []
        for j in range(len(a1)):
            k.append(a1[j][0])
            k.append(a1[j][1])
        
        a1 = list(k)
        result.append(a1)
        
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