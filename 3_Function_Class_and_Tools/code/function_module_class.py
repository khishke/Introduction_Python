#%% Functions

def myFunc(myInput):
    # Basic function
    """
    This function does ...
    Input:
    Output
    """
    print("Hi")
    twice = myInput * 2
    return twice

def two_times(number):
    # Function name is good when short, meaningful and easy to read
    """
    multiple by two
    input: a number
    output: a number
    """
    twice = number*2
    
    return twice 

def my_function(salary, age):
    # Prototype docstring
    """
    
    Purpose of the function is ...

    Parameters
    ----------
    salary : float
        salary of an employee
    age : int
        age of an employee

    Returns
    -------
    int
        twice the first input.


    copyright @Py4Econ
    
    """

def two_three_times_tuple(number):
    # multiple output as tuple
    """
    multiply by two and three
    """
    first = number*2
    second = number*3
    return first, second
    # return number*2, number*3 # tuple

def two_three_times_list(number):
    # multiple output as list
    """
    multiply by two and three
    return list
    """
    #return number*2, number*3 # tuple
    return [number*2, number*3] # list

def aging(age=25, year = 93):
    # default arguments
    """
    """
    
    print("Age is {}".format(age))
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10

def aging1(year,age=25):
    # positional (keyword) and default arguments
    """
    """
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10

def aging2(year, year1, age=25,avar = 17):
    # positional and default arguments
    """
    """    
    print("Age is %d and avar is %d. Name is %s" % (age,avar,"Bat"))
    
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10, year1 +10, avar-5

def aging_args(*args):
    #optional (or arbitrary) positional arguments
    print("hi")
    if len(args) > 3:
        print(args[2])
    elif len(args) > 0:
        print(args[0])
    else:
        print('No optional argument. Stopping.')

# def aging_args2(year=3, year1, age=25,avar = 17,*args): SyntaxError: non-default argument follows default argument
def aging_args2(year, year1, age=25,avar = 17,*args):
    #optional (or arbitrary) positional arguments
    print("hi")
    print(args[0])
    print(args[2])
    
def aging_kwargs(**kwargs):
    #optional (or arbitrary) keyword arguments
    print("hi")
    print(kwargs['numberChild'])
    print(kwargs['nkeys'])

def aging_kwargs2(**kwargs):
    #optional (or arbitrary) keyword arguments
    print("hi")
    # print(kwargs['numberChild'])
    if 'numberChild' in kwargs.keys():
        print("numberChild exists") 
    elif 'nkeys' in kwargs.keys():
        print("use nkeys")
    else: 
        print("do nothing with numberChild and nkeys")
    
    
result = myFunc(10)   # basic
print(result)         # print to terminal
print(two_times(150)) # intelligible function name
help(my_function)     # prototype docstring
# print(my_function())  # error: arguments required
print(two_three_times_tuple(15)) # multiple output as tuple
print(two_three_times_list(15))  # multiple output as list
help(two_three_times_list)
print(aging())        # default values will be taken 
print(aging(35,17))   # can overwrite default values
print(aging1(5))      # must assign positional argument
print(aging2())       # error: must assign positional argument
print(aging2(93,95))  # must assign positional argument
print(aging_args(15,25,35)) # any arguments, should be accessed by position
print(aging_args2(85,75,15,25,35,23,25)) # any arguments, should be accessed by position
print(aging_kwargs(numberChild = 3, nkeys = 5)) # any keyword arguments
print(aging_kwargs2(nkeys=5)) # example of any keyword arguments
print(aging_kwargs2(nbold=15)) # example of any keyword arguments

## Scope of variables
# local scope
x = 20 # global by default

def my_func(ageby=5):
    
    x = 5 # local by default 
    x = x + ageby
    return x

print(x)   # global
res = my_func() # shouldn't change the global
print(res) # x is changed as local
print(x)   # x is still unchanged as global

# global scope
x = 20 # global by default

def my_func(ageby=5):
    
    global x # use global variable inside a function
    x = x + ageby
    return x

print(x)   # global 
res = my_func() # should change the global
print(res) # x is changed inside the function
print(x)   # x is changed as global
 


## Module

# importing modules
import pandas as pd # pd can be pds or whatever you want 
import pandas      # then should use pandas.DataFrame not pd.DataFrame
import numpy as np  

import os # operating system functionality is contained
print(os.getcwd()) # current working directory will be printed

# setting main dir is useful
m_dir = r"D:\\Documents\\python\\repo\\Introduction_Python\3_Function_Class_and_Tools"

# Path
import sys # system parameters
print(sys.path) # all folders in path 
sys.path.append(m_dir + os.sep + 'module') # add folder to path
print(sys.path) # all folders in path 
sys.path.remove(m_dir + os.sep + 'module') # remove folder from path

sys.path.append(m_dir + os.sep + 'module') # add folder to path

# import
import my_mod
print(my_mod.mmod_func(5))

help(my_mod)
del my_mod

import my_mod as mm
print(mm.mmod_func(5))


# import specific function
from my_mod import mmod_funcA as myA
myA(53)

# import all as system level functions
from my_mod import * 
mmod_funcA(5)

# same with pandas or other packages
from pandas import *
# read_csv()
del pandas



## Class
# OOP
class Person:
    "This is a person class"
    age    = 20 
    height = 175

    # method == function
    def greet(self):
        print('Hello')

bold = Person() # instantiation
print(bold.age)
bold.greet()
Person.greet(bold) # can use class name outside
bold.age = 30      # assign value
print(bold.age)

# add path
import sys
m_dir = r"D:\\Documents\\python\\repo\\Introduction_Python\3_Function_Class_and_Tools"
sys.path.append(m_dir + os.sep + 'module') # add folder to path
from my_class import *
# alternative
# from my_class import Hotel 

# Instantiation
iHotel = Hotel(150,100,3)


print(iHotel.nGuest)     # number of guest, variable
print(iHotel.getInfo())  # getInfo method
print(iHotel.__hidVar)   # private (hidden) variable with __ prefix
print(iHotel.dispHid())  # see private variable through a method

iHotel.setGuest(350)     # setGuest method
print(iHotel.nGuest)     # number of guest, variable
print(iHotel.getGuest()) # number of guest, variable

iHotel.setRoom(18)       # setRoom method
iHotel.setHall(2)        # setHall method
print(iHotel.getInfo())  

iBig = bigHotel()      # child class 

print(iBig.nGuest)     # number of guest, variable
print(iBig.getInfo())  # getInfo method
print(iBig.__hidVar)   # private (hidden) variable with __ prefix
print(iBig.dispHid())  # see private variable through a method

iBig.setGuest(350)     # setGuest method
print(iBig.nGuest)     # number of guest, variable

iBig.setRoom(18)       # setRoom method
iBig.setHall(2)        # setHall method
print(iBig.getInfo())  
print(iBig.getNumber())# total number of all

    