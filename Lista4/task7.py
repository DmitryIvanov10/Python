<<<<<<< HEAD
# Lesson4, Task7

# Function which takes any amount of positional and key arguments and prints them
def myFunc(*args, **kwargs):
    # Print positional elements
    i = 0
    for item in args:
        i += 1
        print ("%i -> %s" % (i, str(item)))

    # Print key elements
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))

# Create list for posisional elements 
myList = [1234, 432, 43, 'a', 'sas']

# Create dictionary for key elements 
myDict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 123
}

# Run my function
=======
# Lesson4, Task7

# Function which takes any amount of positional and key arguments and prints them
def myFunc(*args, **kwargs):
    # Print positional elements
    i = 0
    for item in args:
        i += 1
        print ("%i -> %s" % (i, str(item)))

    # Print key elements
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))

# Create list for posisional elements 
myList = [1234, 432, 43, 'a', 'sas']

# Create dictionary for key elements 
myDict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 123
}

# Run my function
>>>>>>> 0b1190fafe0f850c1325c7e615b1abd120588142
myFunc(*myList, **myDict)