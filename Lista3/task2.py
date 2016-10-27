# Lesson3, Task2

# Create a list of squares
squares = (i**2 for i in range(1, 100))

# Print the list
for i, number in enumerate(squares):
    print(str(i+1) + " -> " + str(number))