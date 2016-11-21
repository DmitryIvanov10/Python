"""Module for arithmetic progression"""

def nth_element(a1=0, r=0, n=0):
    """Calculate n-th element of the arithmetic progression"""
    return a1 + (n-1) * r

def n_sum(a1=0, r=0, n=0):
    """Calculate sum of first n elements of the arithmetic progression"""
    return n * (a1 + nth_element(a1, r, n)) / 2