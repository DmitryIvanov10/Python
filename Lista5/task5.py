# Lesson5, Task5

# import own module 
import rgb_hex_convert as convert

# print results
print ("Give values correctly. There is no built in check for wrong input.")
print ()
print ("Give RGB value to convert into HEX.")
r = eval(input("R = "))
g = eval(input("G = "))
b = eval(input("B = "))
hex_number = convert.rgb_to_hex(r, g, b)
print ()
print ("{}.{}.{} in HEX is {}".format(r, g, b, hex_number))
print ()
print ("Give HEX value to convert into RGB")
hex_number = input("HEX = ").upper()
r, g, b = convert.hex_to_rgb(hex_number)
print ("{} in RGB is {}.{}.{}".format(hex_number, r, g, b))