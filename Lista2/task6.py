# Lesson2, Task6

import sys

# check memory size 
print ("Memory size of 0: %i" % sys.getsizeof(0))
print ()
print ("Memory size of 1: %i" % sys.getsizeof(1))
print ()
print ("Memory size of 2**100: %i" % sys.getsizeof(2**100))
print ()
print ("Memory size of 2**1000: %i" % sys.getsizeof(2**1000))
print ()
print ("Memory size of 'True': %i" % sys.getsizeof(True))
print ()
print ("Memory size of 'False': %i" % sys.getsizeof(False))
print ()

# check 'isinstance' expressions
print ("0 is and integer: %s" % isinstance(0, int))
print ("0 is and floating point number: %s" % isinstance(0, float))
print ("0.0 is and floating point number: %s" % isinstance(0.0, float))
print ("'True' is a boolean: %s" % isinstance(True, bool))
print ("'True' is an integer: %s" % isinstance(True, int))