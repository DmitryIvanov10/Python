# Lesson8, Task4

# import from modules
from os import path

# function to read lines into lists - each line would be an element
def file_to_list(file_name, list_name):
    """Read from file file_name to the list list_name"""
    try: 
        # open file to read info from
        with open(file_name, 'r') as f:
            for line in f:
                if line[0] != "#":
                    list_name.append(line)
    except:
        print ("No file {}.".format(file_name))

# read lists of students from files into list variables
python_students = []
file_to_list("students_python.txt", python_students)
python_students = set(python_students)

cpp_students = []
file_to_list("students_cpp.txt", cpp_students)
cpp_students = set(cpp_students)

# create the list of the students in both lists
same_students = list(python_students & cpp_students)

# print the list of students on both subjects
for student in same_students:
    print (student)

