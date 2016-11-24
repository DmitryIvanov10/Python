# Lesson6, Task4

# constant for accuracy of calculations
epsilon = 0.01

def horner_polynom(value, coefficients):
    """Calculate polynom value with Horner algorythm
       Parameters are coefficients of the polynom and a value to calculate for"""
    polynom = 0
    for a in coefficients:
        polynom = polynom * value + a
    return polynom

def change_sides(sides, new_side):
    """Changes one of the sides so function has different signs on two sides"""
    if horner_polynom(new_side, coefficients) * \
       horner_polynom(sides[0], coefficients) < 0:
        sides[1] = new_side
    else:
        sides[0] = new_side

# initial data 
coefficients = [1, 2, -4, -10]
sides = [1, 3]

run = True

while run:
    # check if 0 on one of the sides
    for i in range(2):
        if abs(horner_polynom(sides[i], coefficients)) < epsilon:
            # save zero point value
            zero = sides[i]
            # print results
            print ("Zero point is {}".format(zero))
            print ("f({}) = {}".format(sides[i], \
                   round(horner_polynom(sides[i], coefficients), 3)))
            run = False
        
    # check if signs on two sides are different
    if horner_polynom(sides[0], coefficients) * \
       horner_polynom(sides[1], coefficients) > 0:
        print ("No zero places.") 
        run = False
    
    # devide interval into half
    x = (sides[0] + sides[1]) / 2

    # change sides depending on the value of the function in the middle of the interval
    change_sides(sides, x)  
    