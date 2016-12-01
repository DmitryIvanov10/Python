# Lesson7, Task2

# import data from modules
from sys import argv
from temperatures import random_celsius_degree

# max temperature in Celsius degrees
max_T = 300

# Check if user input is correct
if len(argv) != 2:
    print ("Wrong amount of arguments.")
elif not argv[1].isdigit():
    print ("Wrong data for amount of generating temperatures")
else:
    # amount of generating temperatures
    n = int(argv[1])

    # create file to write data to (and clear if necessary)
    with open("celsius.txt","a+") as f:
        # clear the file
        open("celsius.txt","w").close()

        # add a line with commentaries to file
        f.write("# Temperature in Celsius\n")

        # add temperature data to file
        for i in range(n):
            f.write("{}\n".format(random_celsius_degree(max_T)))