# Lesson 10, Task4

# get input from user 
print ("Print Your text and press enter:")
text = input()

# vowels
vowels = ["a", "e", "i", "o", "u", "y"]

# variable for amount of vowels in text
amount_of_vowels = 0

# calculate amount of vowels in text
for letter in text:
    if letter in vowels: 
        amount_of_vowels += 1

# print results
print ("There are {} vowels in Your text.".format(amount_of_vowels))