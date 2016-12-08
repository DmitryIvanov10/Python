# Lesson8, Task1

# import data from modules
from sys import argv
from sys import exit

# constant name of the file 
file_name = 'result1.txt'

# list comprehension function
def list_comprehension(n):
    """Creates list of numbers of the type n/(n+1)""" 
    return [i/(i+1) for i in range(1, n+1)]

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

    # create list of numbers
    my_list = list_comprehension(n)
  
    # open file to read info from
    with open(file_name, 'a+') as f:
        # clear the file 
        open(file_name, 'w').close() 

        # write the first line in file()
        f.write("# First {} elements of an array n/(n+1): \n".format(n))        

        # write info to te file
        for i, element in enumerate(my_list):
            f.write("a{} = {} \n".format(i+1, round(element,2)))