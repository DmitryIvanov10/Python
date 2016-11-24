# Lesson6, Task2

def get_number():
    """Gets number from user, check if input in a natural number"""
    n = ""
    while not n.isdigit():
        n = input("Give natural number: ")
    return eval(n) 

def is_prime(n):
    """Checks if a given number n is a prime number"""
    prime = True
    d = 2
    while prime and d <= round(n**(1/2)):
        if n%d != 0:
            d += 1
        else:
            prime = False
    return prime
    
# get data from user
number = get_number()

# print result
if is_prime(number):
    print ("{} is a prime number.".format(number))
else:
    print ("{} is not a prime number.".format(number))