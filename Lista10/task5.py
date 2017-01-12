# Lesson10, Task5

# import modules
from sys import argv
import os

# get file directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# check if correct amount of arguments
if len(argv) != 3:
    print ("Wrong amount of arguments.")

# check if arguments are correct    
elif argv[1][-4:] != ".txt":
    print ("Wrong file extension.")
else:
    # add the file name to the directory path
    dir_path += "\\" + argv[1]
    
    # add a new line to the document
    with open(argv[1], 'a+') as file:
        # if document exist - add on new line
        if os.path.isfile(dir_path) and os.path.getsize(dir_path) > 0:
            file.write("\n" + argv[2])
        else:
            # if document doesn't exist - add first line
            file.write(argv[2])