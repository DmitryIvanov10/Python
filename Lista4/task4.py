<<<<<<< HEAD
# Lesson4, Task4

# Function to print first N Fibonacci numbers
def printFibonacci(N):
    if N < 1:
        print ("You gave the wrong amount of Fibonacci numbers.")
    else:    
        f1 = 0
        f2 = 1
        for i in range(N):
            print (f1)
            f = f2
            f2 = f1 + f
            f1 = f

# Example 
=======
# Lesson4, Task4

# Function to print first N Fibonacci numbers
def printFibonacci(N):
    if N < 1:
        print ("You gave the wrong amount of Fibonacci numbers.")
    else:    
        f1 = 0
        f2 = 1
        for i in range(N):
            print (f1)
            f = f2
            f2 = f1 + f
            f1 = f

# Example 
>>>>>>> 0b1190fafe0f850c1325c7e615b1abd120588142
printFibonacci(10)