<<<<<<< HEAD
# Lesson4, Task6

# Function with three key elements in the end 
def myFunc(*args, kwarg1, kwarg2, kwarg3):
    print ("*Args =", args)
    print ("Pre pre last element is", kwarg1)
    print ("Pre last element is", kwarg2)
    print ("Last element is", kwarg3)

# Example 
=======
# Lesson4, Task6

# Function with three key elements in the end 
def myFunc(*args, kwarg1, kwarg2, kwarg3):
    print ("*Args =", args)
    print ("Pre pre last element is", kwarg1)
    print ("Pre last element is", kwarg2)
    print ("Last element is", kwarg3)

# Example 
>>>>>>> 0b1190fafe0f850c1325c7e615b1abd120588142
myFunc(123, 321, '324', True, 123, 'asd', kwarg1 = 'Key1', kwarg2='key2', kwarg3='key3')