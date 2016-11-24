# Lesson6, Task1

# initial data
a1 = 1.1
q = 1.5
n = 100

# create list of geometric progression elements
def create_geometric_progression(a1, q, n):
    """Generates n elements of geometric progression 
    for given first element a1 and common ratio q"""
    new_list = [a1]
    for i in range(1, n):
        new_list.append(new_list[i-1]*q)
    return new_list

my_geometric_progression = create_geometric_progression(a1, q, n)

# print results
for i,element in enumerate(my_geometric_progression):
    print ("a{} = {}".format(i+1, round(element,2)))
print ()
for i,element in enumerate(my_geometric_progression[1::2]):
    print ("a{} = {}".format(i*2+2, round(element,2)))