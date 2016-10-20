# Lesson2, Task2
# -*- coding: utf-8 -*-

# create list of students
students = ["Kasia", "Basia", "Marek", "Darek"]

# add student using append 
students.append("Jożek")

# add student using extend 
students.extend(["Ania", "Basia"])

# sort list of students
students.sort()

# print list of students
print (students)
print ()

# print fourth student in the list
print ("Fourth student is %s" % students[3])
print ()

# print first two
print ("First two students are %s and %s" % (students[0], students[1]))
print ()

# print last two
print ("Last two students are %s and %s" % (students[len(students) - 2] \
                                           , students[len(students) - 1]))
print ()

# remove students with name Basia from the list
name = "Basia"
while name in students:
    students.remove(name)

# print amount of students
print ("There are %i students in the list." % len(students))

# make a tuple from the list
students = tuple(students)