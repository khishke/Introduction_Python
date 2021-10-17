# OOP
class Person:
    "This is a person class"
    age = 10 
    appearance = "cool"

    # method == function
    def greet(self):
        print('Hello')

bold = Person()
bold.age
bold.greet()
Person.greet(bold)


import sys
from week3.module.my_class import bigHotel 
sys.path.append(r"C:\Users\sugarkhuu\Documents\python\repo\Introduction_Python\week3\module")


# from my_class import Hotel
from my_class import *
iHotel = Hotel(150,100,3)
print(iHotel.nGuest)
print(iHotel.getInfo())

ex_big = bigHotel()
