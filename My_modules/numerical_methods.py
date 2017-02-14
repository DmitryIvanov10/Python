"""Module for numerical calculations"""
import numpy as np
from math import pi

def g(_f, a, b, c):
    """Returns value of the function depending on a,b,c"""
    return -( a*_f(b)*_f(c)*(_f(b)-_f(c)) + \
              b*_f(c)*_f(a)*(_f(c)-_f(a)) + \
              c*_f(a)*_f(b)*(_f(a)-_f(b)) ) / \
            ( (_f(a)-_f(b)) * (_f(b)-_f(c)) * (_f(c)-_f(a)) )

def bisection(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by bisection method"""
    """Returns zero place and number of iterations (x, iterations)""" 
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1    

        # devide interval into half
        c = (_a + _b) / 2

        # check if 0 on the division point
        if abs(_f(c)) < _eps:
            x = c
            return x, iterations

        # change sides depending on the value of the function in the middle of the interval
        if _f(c) * _f(_a) > 0:
            _a = c
        else:
            _b = c

        if iterations > 1/_eps:
            print ("No zero places.")
            return 0, -1

def brent(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by Brent method""" 
    """Returns zero place and number of iterations (x, iterations)"""
    # check if signs on two sides are different
    if _f(_a) * _f(_b) > 0:
        print ()
        print ("No zero places.") 
        print ()
        return 0, -1

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1    

        # devide interval
        if  iterations == 1 or x > _b or x < _a:
            c = (_a + _b) / 2
        elif abs(_f(c)) < _eps:
            return x, iterations
        else:
            c = x 

        # calculate possible x for Brent method (parabola from three points)
        x = g(_f, _a, _b, c) 

        # change sides depending on the value of the function in the middle of the interval
        if _f(c) * _f(_a) < 0:
            _b = c
        else:
            _a = c    

def secant(_f, _a, _b, _eps = 0.0001):
    """Finds zero place of function _f if possible in interval [_a, _b] 
    with precision _eps by secant method""" 
    """Returns zero place and number of iterations (x, iterations)"""

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1  

        # find next element and reset previous
        _a, _b = _b, _b - _f(_b) * (_b - _a) / (_f(_b) - _f(_a))

        if abs(_f(_b)) < _eps:
            return _b, iterations

def newton(_f, _a, _eps = 0.0001):
    """Finds zero place of function _f if possible from x0 = _a 
    with precision _eps by Newton method""" 
    """Returns zero place and number of iterations (x, iterations)"""

    # iteration parameteres
    iterations = 0

    while True:
        # calculate iteration
        iterations += 1  

        # find next element and reset previous
        b = _a - _f(_a) * _eps / (_f(_a + _eps) - _f(_a))

        if abs(b - _a) < _eps:
            return b, iterations
        else: 
            _a = b

def simpson(_f, _a, _b, n = 20, _eps = 0.0001):
    """Finds numerically definite integral of function in the interval [_a, _b]
    with precision _eps and returns the value of the integral"""
    """By default amount of nodes is 20"""
    
    # calculate step
    h = (_b - _a) / (n - 1)  

    # variable for the result value
    result = 0

    # main loop
    for i in range(n):
        # first or last element
        if i==0 or i==n-1:
            result += _f(_a)
        # odd element
        elif i % 2 == 1:
            result += 4 * _f(_a)
        # even element    
        else:
            result += 2 * _f(_a)
        # do step
        _a += h

    return result * h / 3

def trapeze(_f, _a, _b, n = 20, _eps = 0.0001):
    """Simpson method to calculate definite integral numerically"""
    """Finds numerically definite integral of function in the interval [_a, _b]
    with precision _eps and returns the value of the integral"""
    """By default amount of nodes is 20"""
    
    # calculate step
    h = (_b - _a) / (n - 1)  

    # variable for the result value
    result = 0

    # main loop
    for i in range(n):
        # first or last element
        if i==0 or i==n-1:
            result += 0.5 * _f(_a)
        # other elements
        else:
            result += _f(_a)
        # do step
        _a += h

    return result * h

def rad_to_grad(_alpha):
    """Changes angle in radians into grads"""
    return _alpha * 180 / pi

def grad_to_rad(_alpha):
    """Changes angle in radians into grads"""
    return _alpha * pi / 180

def gauss_legendre_integral(_f, _a, _b, _n):
    """Calculates and returns integral by Gauss-Legendre quadratures method 
    for function _f in interval of [_a, _b] and for n = _n""" 
    # calculate abscissae and weights
    x, c = np.polynomial.legendre.leggauss(_n)

    # change interval from [-1, 1] to [_a, _b]
    t = []
    s = 0
    for i in range(len(x)):
        t.append(0.5 * (_b - _a) * x[i] + 0.5 * (_b + _a))
        s += _f(t[i])*c[i]

    return 0.5 * (_b - _a) * s