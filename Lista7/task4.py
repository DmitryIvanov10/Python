# Lesson7, Task4

# import data from modules
from temperatures import convert_F_to_C

# create lists to save data about temperatures
degrees_in_F = []
degrees_in_C = []

# read from file "fahrenheit.txt"
with open("fahrenheit.txt","r") as f_F:
    for line in f_F:
        if line[0] != "#":
            # add info to the list of degrees is Fahrenheit
            degrees_in_F.append(float(line))

# read from file "celsius.txt"
with open('celsius.txt', 'r') as f_C:
    for line in f_C:
        if line[0] != "#":
            # add info to the list of degrees is Celsius
            degrees_in_C.append(float(line))

# variables to check if degrees are converted correctly
check = True
i = -1

# check if both lists are of the same length
n = len (degrees_in_C)
m = len (degrees_in_F)

if m!=n:
    check = False

# compare results in both files
while check and i < len(degrees_in_F) - 1:
    i += 1
    if degrees_in_C[i] != convert_F_to_C(degrees_in_F[i]):
        check = False

# print results
if check:
    print ("Degrees converted correctly.")
else:
    print ("Degrees converted incorrectly.")