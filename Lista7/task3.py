# Lesson7, Task3

# import data from modules
from temperatures import convert_C_to_F

# create file to write data to (and clear if necessary)
with open("fahrenheit.txt","a+") as f_F:
    # clear the file
    open("fahrenheit.txt","w").close()
    f_F.write("# Temperature in Fahrenheit\n")

    # read from file "celsius.txt"
    with open('celsius.txt', 'r') as f_C:
        for line in f_C:
            if line[0] != "#":
                f_F.write("{}\n".format(convert_C_to_F(float(line))))
