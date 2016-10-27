# Lesson1, Task7

# strip() method 
# removes given chars from the beginning and the end of the string 
stringForStrip = "fffHello World!ffff"
print (stringForStrip.strip("f"))
print()

# isnumeric() method
# checks whether the string consists of only numeric characters 
# u character changes the string into unicode
# example with non numeric string
stringForIsnumeric = u"asdj23jcv4"
print (stringForIsnumeric.isnumeric())
print()

# example with numeric string
stringForIsnumeric = u"234597345"
print (stringForIsnumeric.isnumeric())
print()

# rjust() method 
# return right justified string of given width adding given characters on the left (space as default)
# returns original string if its length is bigger than given for rjust()
stringForRjust = "My string."
print (stringForRjust.rjust(20, 'A'))