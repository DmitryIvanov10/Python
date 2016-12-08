# Lesson8, Task2

# import data from modules
from sys import argv
from sys import exit

# constant name of the file 
file_name = 'result2.txt'

# number generator function
def my_generator(n):
    """Generates numbers of type n/(n+1)"""
    """i = 1
    while i < n+1:
        yield i/(i+1)
        i += 1 """
    return (i/(i+1) for i in range(1, n+1))

# check if user input is correct
if len(argv)!=2:
    # check amount of arguments
    print ("Wrong amount of arguments.")
else:
    # amount of numbers
    try:
        n = eval(argv[1])
    except:
        exit(1)

    # open file to read info from
    with open(file_name, 'a+') as f:
        # clear the file 
        open(file_name, 'w').close() 

        # write the first line in file()
        f.write("# First {} elements of an array n/(n+1): \n".format(n))        

        # declare generator 
        gen = my_generator(n)

        # write info to te file
        """for i in range(1, n+1):
            f.write("a{} = {} \n".format(i, round(next(gen),2)))"""
        for i, element in enumerate(gen):
            f.write("a{} = {} \n".format(i+1, round(element,2)))