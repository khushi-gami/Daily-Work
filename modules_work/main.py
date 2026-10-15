from datetime import date 
import math_utils as calculation

print("addition : ",calculation.add(30,50))
print("substraction : ",calculation.subtract(30,50))
print("multiplication : ",calculation.multiply(30,50))
print("division : ",calculation.divide(30,50))

import math as m

print("square root of (49) : ",m.sqrt(49))

angle = m.radians(90)
print("90 value in sin : ",m.sin(angle))

import string_utils

print("no. of vowels in the string : ",string_utils.vowles_count("bharati"))

import greet

greet.greet_msg("shivani")

import helper

helper.result(97)
helper.factorial(4)

from shapes import circle

circle.circle_area(4)

from shapes import rectangle

rectangle.ractangle_area(10,30)

from utilities import file_utils

file_utils.writefile("modules_work/utilities/demo.txt","This is text demo file !")

print("file ocntent : ",file_utils.readfile("modules_work/utilities/demo.txt"))

from utilities import date_utils

date1 = date(2024,10,15)
date2 = date (2024,11,8)

print("difference between to days : ",date_utils.date_difference(date1,date2))

print(dir(m))

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
student = Student("khushi","98")
print(dir(student))

import geometry

print("circle area : ",geometry.circle_area(20))
print("circle circumference : ",geometry.circumference(40))

print("triangle area : ",geometry.triangle_area(10,30))
print("triangle perimeter : ",geometry.perimeter(10,20,30))
