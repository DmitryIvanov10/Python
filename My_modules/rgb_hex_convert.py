"""Module to convert between RGB and HEX"""

"""Changes two-digit numbers into letters"""
_number_to_letter = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

"""Changes letters into two-digit numbers"""
_letter_to_number = {
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15
}

def _number_to_hex(number):
    """Changes 8-bit number into HEX"""
    a1 = number // 16
    a0 = number % 16
    if a1 > 9:
        a1 = _number_to_letter[a1]
    if a0 > 9:
        a0 = _number_to_letter[a0]
    return str(a1) + str(a0)

def _hex_to_number(hex_number):
    """Changes double-value HEX into 8-bit number"""
    a1 = hex_number[0]
    a0 = hex_number[1]
    if a1.isdigit():
        a1 = eval(a1)
    else:
        a1 = _letter_to_number[a1]
    if a0.isdigit():
        a0 = eval(a0)
    else:
        a0 = _letter_to_number[a0]
    return 16 * a1 + a0

def rgb_to_hex(r, g, b):
    """Convert from RGB to HEX"""
    return _number_to_hex(r) + \
           _number_to_hex(g) + \
           _number_to_hex(b)

def hex_to_rgb(hex_number):
    """Convert HEX to RGB"""
    return _hex_to_number(hex_number[:2]), \
           _hex_to_number(hex_number[2:4]), \
           _hex_to_number(hex_number[4:])