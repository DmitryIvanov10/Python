"""Module to convert between Celsius and Fahrenheit temperatures. 
Also generates random temperature values."""

# import data from module
from random import random

# absolute zero const
_zero = -273.15

def convert_C_to_F (degree):
    """Convert Celsius degrees to Fahrenheit degrees"""
    return round(degree*9 / 5 + 32, 2)

def convert_F_to_C (degree):
    """Convert Fahrenheit degrees to Celsius degrees"""
    return round((degree - 32)*5 / 9, 2)

def random_celsius_degree(T):
    """Generates random degree in Celsius up to temperature T"""
    return round(random()*(T - _zero) + _zero, 2)