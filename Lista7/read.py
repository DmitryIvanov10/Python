# Lesson7, Task5

# import data from modules
from sys import argv
from os import path

# Check if user input is correct
if len(argv)<2 or len(argv)>3:
    # check amount of arguments
    print ("Wrong amount of arguments.")
else:
    # get file name
    file_to_read = argv[1]

    # check if file exists
    if not path.isfile(file_to_read):
        print ("No such file.")
    else:
        # default mode
        mode = 0

        # check for mode
        if len(argv) == 3:
            if argv[2] != "1" and argv[2] != "2" and argv[2] != "0":
                print ("Wrong mode.")
            else:
                mode = int(argv[2])

        # open file to read info from
        with open(file_to_read, 'r') as f:
            # print open message
            print ()
            print ("Printing from file {} in mode {}".format(file_to_read, mode))
            print ()

            # print info depending on the mode
            if mode == 0:
                print (f.read())
            elif mode == 1:
                for line in f:
                    if line[0] != "#":
                        print (line)
            else:
                for i, line in enumerate(f):
                    print ("{}. {}".format(i+1, line))