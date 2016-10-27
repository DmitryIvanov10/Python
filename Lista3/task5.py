# Lesson3, Task5
# Guess number game

from random import randint

# Range and differences
minimum = 0
maximum = 100
bigDifference = (maximum-minimum) // 2
mediumDifference = (maximum-minimum) // 10

# Generate the random number
randomNumber = randint(minimum, maximum)

# If true - continue game
run = True 
numberOfGuesses = 0

# Game instructions
print ("This is the guess number game. \n\n\
Try to guess integer number between [%i,%i].\n\n\
Program would help You guess:\n\n\
Much bigger: more than %i up;\n\
Bigger: %i to %i up;\n\
A bit bigger: 1 to %i up;\n\
A bit smaller: 1 to %i down;\n\
Smaller: %i to %i down;\n\
Much smaller: more than %i down.\n\n"\
% (minimum,maximum,bigDifference,mediumDifference+1,bigDifference,\
   mediumDifference,mediumDifference,mediumDifference+1,\
   bigDifference,bigDifference))

while run:
    # Ask user to guess number and get it
    print ("Guess the number: ", end = '')
    userGuess = eval(input())

    # Calculate number of guesses
    numberOfGuesses += 1

    difference = userGuess - randomNumber

    if userGuess<minimum or userGuess>maximum:
        print ("Your guess is not in a range!\n\n")
    elif difference > bigDifference:
        print ("The number is much smaller.\n\n")
    elif difference > mediumDifference:
        print ("The number is smaller.\n\n")
    elif difference > 0:
        print ("The number is a bit smaller.\n\n")
    elif difference < -bigDifference:
        print ("The number is much bigger.\n\n")
    elif difference < -mediumDifference:
        print ("The number is bigger.\n\n")
    elif difference < 0:
        print ("The number is a bit bigger.\n\n")
    else:
        print ("Congratulations, You've guessed the number.")
        print ("It took You %i tries." % numberOfGuesses)
        run = False