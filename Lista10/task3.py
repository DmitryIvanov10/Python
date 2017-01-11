# Lesson10, Task3

def volume(*args):
    """Returns the volume of the cuboid"""
    """If 1 arguments - the volume of cube with side which is argument"""
    """If 3 arguments - the volume of random cuboid with sides which are arguments"""
    if len(args) == 1:
        return args[0]**3
    elif len(args) == 3:
        return args[0]*args[1]*args[2]
    else:
        print ("Wrong amount of arguments.")
        pass

# print results
print ("Volume of cube with the side 10 is {}.".format(volume(10)))
print ("Volume of cuboid with sides 10, 20 and 30 is {}.".format(volume(10, 20, 30)))
print (volume(10, 20))