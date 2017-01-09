"""Module for operations with matricies"""

# function to calculate float as a fraction
from fractions import Fraction 

def print_matrix(matrix):
    """Print the n*n matrix"""
    print ()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).rjust(7), end = '')
        print ()
    print ()

def matrix_multiplication(matrix1, matrix2):
    """Multiply two n*n matricies and returns the matrix of multiplication"""
    if len(matrix1[0]) != len(matrix2):
        return None
    else:
        result_matrix = []
        for i in range(len(matrix1)):
            result_matrix.append([])
            for j in range(len(matrix2[0])):
                x = 0
                for k in range(len(matrix1[0])):
                    x += matrix1[i][k] * matrix2[k][j]
                result_matrix[i].append(x)
        return result_matrix

def determinant(matrix):
    """Returns the determinant of the n*n matrix"""
    # check if matrix is squared
    if len(matrix[0]) != len(matrix):
        return None
    
    new_matrix = [row[:] for row in matrix]
        
    n = len(matrix)
    det = 1
    for i in range(n):
        # change the row if the element on the main diagonal is 0
        # return determinant = 0 if all lower rows are 0 up to main diagonal
        j = i
        while new_matrix[j][i] == 0 and j < n-1:
            j += 1
            if j == n:
                return 0

        # take the row with the highest element in the column
        k = j
        for l in range(k+1, n-1):
            if abs(new_matrix[l][i]) > abs(new_matrix[j][i]):
                j = l

        if j != i:
            for k in range(i,n):
                # change rows, change the sign of the determinant
                new_matrix[i][k], new_matrix[j][k] = new_matrix[j][k], new_matrix[i][k]
            det *= -1

        # make first elements of lower rows equal to 0
        for j in range(i+1, n):
            if new_matrix[j][i] != 0: 
                a = new_matrix[i][i]
                b = new_matrix[j][i]
                for k in range(i, n):
                    new_matrix[j][k] -= new_matrix[i][k]*b/a

    # calculate determinant as a multiplication of diagonal elements
    for i in range(n):
        det *= new_matrix[i][i]
    
    # check for small uncertainties around 0
    if det == 0:
        return 0
        
    return det

def opposite_matrix(matrix):
    """Returns opposite matrix to given n*n matrix"""
    if determinant(matrix) == 0:
        print ("No opposite matrix. Determinant is equal to 0.")
        return [0]
    else:
        result_matrix = []
        for i in range(len(matrix)):
            result_matrix.append([])
            for j in range(len(matrix[0])):
                help_matrix = [row[:] for row in matrix]
                help_matrix.pop(i)
                for k in range(len(matrix)-1):
                    help_matrix[k].pop(j)
                result_matrix[i].append((-1)**(i+j) * determinant(help_matrix) / determinant(matrix))
        for i in range(len(result_matrix)):
            for j in range(i+1, len(result_matrix[0])):
                result_matrix[i][j], result_matrix[j][i] = result_matrix[j][i], result_matrix[i][j]

        return result_matrix

def calculate_coefficients(A,b,name):
    """Returns matrix of coefficients x[] in equation: A[] * x[] = b[]"""
    # calculations x[] = A^(-1)[] * b[]
    result = matrix_multiplication(opposite_matrix(A),b)
    
    #print initial data and answer
    print_matrix(A)
    print("     *     " + name + "     =")
    print_matrix(b)

    for i in range(len(A)):
        print("{}{} = {}".format(name, i, str(*result[i]).rjust(4)))
    print ()
    return result

def solve_equations_by_LU(A, b):
    """Returns matrix of coefficients x[] in equation: A[] * x[] = b[]"""
    # calculations by using LU parts of matrix A
    L,U = matrix_into_LU(A)

    # create empty answer matrix 
    result = []
    for i in range(len(A)):
        result.append([0])

    # calculate z[] matrix to use in solving equation by LU method
    z = []

    for i in range(len(A)):
        sum = 0
        for k in range(i):
            sum += L[i][k]*z[k][0]
        z.append([(b[i][0] - sum) / L[i][i]])

    # calculate result matrix 
    for i in range(len(A)-1, -1, -1):
        sum = 0
        for k in range(2-i):
            sum += U[i][2-k]*result[2-k][0]
        result[i][0] = (z[i][0] - sum) / U[i][i]
        
    return result

def matrix_into_LU(matrix):
    """Returns L and U ratricies of matrix"""
    # check if matrix is squared
    if len(matrix[0]) != len(matrix):
        return None

    # create matricies L and U
    L = []
    U = []
    for i in range(len(matrix)):
        L.append([])
        U.append([])
        for j in range(len(matrix)):
            if j != i:
                L[i].append(0)
            else:
                L[i].append(1)
            U[i].append(0)

    # fill matricies
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            sum = 0
            for k in range(i):
                sum += L[i][k]*U[k][j]
            U[i][j] = matrix[i][j] - sum
        for j in range(i+1, len(matrix)):
            sum = 0
            for k in range(i):
                sum += L[j][k]*U[k][i]
            L[j][i] = (matrix[j][i] - sum) / U[i][i]

    return L, U

def matrix_in_fractions(matrix):
    """Returns same matrix with coefficients in fractions look"""
    """Only works for 1 and 2 dimensional matricies"""
    result = []
    
    if type(matrix) is list:
        if type(matrix[0]) is int or \
           type(matrix[0]) is float:
            for i in range(len(matrix)):
                result.append(Fraction(matrix[i]).limit_denominator())
        elif type(matrix[0] is list):
            for i in range(len(matrix)):
                result.append([])
                for j in range(len(matrix[0])):
                    result[i].append(Fraction(matrix[i][j]).limit_denominator())
    else:
        print ("Wrong initial data!")
        return 0

    return result

def hilbert_matrix(n):
    """Returns Hilbert matrix n*n"""
    result = []

    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(1 / (i+j+1))

    return result

def transpose(matrix):
    """Returns transposed matrix to given"""
    result = []

    for i in range(len(matrix[0])):
        result.append([])
        for j in range(len(matrix)):
            result[i].append(matrix[j][i])
        
    return result

def add_two_dimensional_matricies(matrix1, matrix2):
    """Returns matrix which is a sum of two two dimensional matricies"""
    result = []
    if type(matrix1) is list and \
       type(matrix2) is list and \
       len(matrix1) == len(matrix2) and \
       type(matrix1[0]) is list and \
       type(matrix2[0]) is list and \
       len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            result.append([])
            for j in range (len(matrix1[0])):
                result[i].append(matrix1[i][j] + matrix2[i][j])
        return result
    else:
        print ("Wrong initial data!")
        return [[0]]

def subtract_two_dimensional_matricies(matrix1, matrix2):
    """Returns matrix which is a subtraction of two two dimensional matricies"""
    result = []
    if type(matrix1) is list and \
       type(matrix2) is list and \
       len(matrix1) == len(matrix2) and \
       type(matrix1[0]) is list and \
       type(matrix2[0]) is list and \
       len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            result.append([])
            for j in range (len(matrix1[0])):
                result[i].append(matrix1[i][j] - matrix2[i][j])
        return result
    else:
        print ("Wrong initial data!")
        return [[0]]

def add_one_dimensional_matricies(matrix1, matrix2):
    """Returns matrix which is a sum of two one dimensional matricies"""
    result = []
    if type(matrix1) is list and \
       type(matrix2) is list and \
       len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            result.append(matrix1[i] + matrix2[i])
        return result
    else:
        print ("Wrong initial data!")
        return [0]

def subtract_one_dimensional_matricies(matrix1, matrix2):
    """Returns matrix which is a subtraction of two one dimensional matricies"""
    result = []
    if type(matrix1) is list and \
       type(matrix2) is list and \
       len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            result.append(matrix1[i] - matrix2[i])
        return result
    else:
        print ("Wrong initial data!")
        return [0]