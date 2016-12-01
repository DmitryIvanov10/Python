"""Module to convert between Celsius and Fahrenheit temperatures. 
Also generates random temperature values."""

from random import random

def convert_C_to_F (degree):
    return round(degree*9 / 5 + 32, 2)

def convert_F_to_C (degree):
    return round((degree - 32)*5 / 9, 2)

def random_celsius_degree():
    return round(random()*573.15 - 273.15, 2)