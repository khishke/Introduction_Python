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
    input
    output
    """
    twice = number*2
    
    return twice 

def my_function(input1, input2):
    # Prototype docstring
    """
    
    Purpose of the function

    Parameters
    ----------
    input1 : float
        salary of employee
    input2 : int
        age of employee

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
    # first = number*2
    # second = number*3
    # return first, second
    return number*2, number*3 # tuple

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
    "Age is %d and avar is %d. Name is %s" % (age,avar,"Bat")
    
    print("Age is %d and avar is %d. Name is %s" % (age,avar,"Bat"))
    
    age_10 = age + 10
    year_10 = year + 10
    return age_10, year_10, year1 +10, avar-5

def aging_args(*args):
    #optional (or arbitrary) positional arguments
    print("hi")
    print(args[0])
    print(args[2])

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

#%% Scope of variables
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
 


#%% Module

# importing modules
import pandas as pd # pd can be pds or whatever you want 
import pandas      # then should use pandas.DataFrame not pd.DataFrame
import numpy as np  

import os # operating system functionality is contained
print(os.getcwd()) # current working directory will be printed

# setting main dir is useful
m_dir = r"C:\Users\sugarkhuu\Documents\python\repo\Introduction_Python_Nov21"

# Path
import sys # system parameters
print(sys.path) # all folders in path 
sys.path.append(m_dir + os.sep + 'week3\module') # add folder to path
print(sys.path) # all folders in path 
sys.path.remove(m_dir + os.sep + 'week3\module') # remove folder from path

sys.path.append(m_dir + os.sep + 'week3\module') # add folder to path

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



#%% Class
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
m_dir = r"C:\Users\sugarkhuu\Documents\python\repo\Introduction_Python_Nov21"
sys.path.append(m_dir + os.sep + 'week3\module') # add folder to path
from my_class import *
# alternative
# from module.my_class import Hotel 

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



#%% One-liner, lambda, zip, enumerate
import numpy as np

## one-liner

# for loop
# long 
mlist = [] 
for i in range(10):
    print(i)
    mlist.append(i)
print(mlist)

# one line
mmlist = [i for i in range(10)]    
print(mmlist)

# if
status = False
# long
if status:
    xvar = 5
else:
    xvar = 4
    
# one-line
yvar = 5 if status else 4

# if else and for loop
# long
mlist = []
for i in range(10):
    if np.mod(i,2)==0:
        mlist.append(i)
    else:
        mlist.append(i-1)
print(mlist)

# one line
lst = [i if np.mod(i,2)==0 else i-1 for i in range(0,10)]
print(lst)


## lambda 

func = lambda a : a + 10
func(5)

# filter
def pos(input1):
    return True if input1 >0 else False

res = list(filter(pos,[1,-10,3,-7,4,-9]))

def neg(input1):
    return False if input1 >0 else True

res = list(filter(neg,[1,-10,3,-7,4,-9]))

# lambda in filter
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# map
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)

# zip
list1 = range(0,10)
list2 = range(10,20)

for i in zip(list1, list2):
    print(i)  

# enumerate  
for count, value in enumerate(list2):
    print(count, value)
    
for count, value in enumerate(['Michidmaa','Bodio','Nyamdelger']):
    print(count, value)
    
#%% Exception
randomList = ['a', 0, 2]

for entry in randomList:
    try: 
        r = 1/int(entry)
        print(r)
    except:
        print("Error. Can't do conversion because variable is {}, {}".format(entry,type(entry)))

# error system message
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        continue
    print("The reciprocal of", entry, "is", r)

# errors handled differently
for entry in randomList:
    try:
       # do something
        r = 1/int(entry)
        print("Inverse of entry is " + str(r))
    except ValueError:
       # handle ValueError exception
       print('Division by wrong type!')
    except (TypeError, ZeroDivisionError):
       # handle multiple exceptions
       # TypeError and ZeroDivisionError
       print('Division by Zero!')
   

# User defined exception
class myStrangeError(Exception):
    # do correction here
    print("My strange error occurred!")
    
a = 1
try:
    if a > 5:
        a = a + 100 
    else:
        raise myStrangeError()
except myStrangeError:
    print("My strange error occurred!, so adding only 10")
    a = a + 10
except:
    print("Another error occurred!, so adding 1000")
    a = int(a) + 1000

#%% Regular expression
import re

# regex, regexp
# meta characters
# [] . ^ $ * + ? {} () \ |
# 

#special sequences
#https://pynative.com/python-regex-special-sequences-and-character-classes/

# regex tool
# https://regex101.com/


# findall - find all matches within the string
string = 'hello 12 hi 8987. Howdy 34'
pattern = '\d+' # find all numbers
result = re.findall(pattern, string) 
print(result)

re.findall('[D-F]', "LIFE is Cool DARDU") # find CAPITAL letters between D and F

# search – first match anywhere in string
string = "My iPython is fun aPython"
match = re.search('Python', string) # search word Python
match.group()

string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3})\s(\d{2})'
# match variable contains a Match object. 
match = re.search(pattern, string) 

match.group(1)
match.group(2)
match.group(1, 2)
match.groups()


pattern = '\d{3}\s\d{2}'
# match variable contains a Match object. 
match = re.search(pattern, string) 
match.group()


# match - match at the beginning of string
result = re.match("[1-9]{1,3}", "hi 12345 bhey 135456")
result = re.match("[0-9]{1,3}", "12345 dfdf 456")
result.group()


# split
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string) 
print(result)

result = re.split("\s+", "  Baldan   Gombo") 
print(result)


# sub
string = 'abc 12\
de 23 \n f45 6'
pattern = '\s+'
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)


text = "Dorj Bat. He was born on 17th of February, 1995\
Has got bachelor degree. Phone: 99779977, uses Mobicom. \
Graduated 3rd secondary school of Khovd aimag. \
Citizen ID KhO95021701. PIN code of Khan bank card is 0011\
Lives with his wife and two children."


citizenId = re.findall("\w{2,3}(?=\d{8})\d{8}",text)
region    = re.findall(r"(Khovd|Uvs|Zavkhan)",text)
mobileOperator = re.findall(r"(Mobicom|Unitel|Skytel|G-mobile)",text)
mobile_number  = re.findall("(?<=\s)\d{8}",text)
bank           = re.findall("\s(\w*)\sbank",text)
nChild         = re.findall("\s(\w*)\schildren",text)

# ?<= lookbehind, ?= lookahead
# + 1 or more, * 0 or more
# [a-z][A-Z][0-9] - groups
# . any character, \ escape

# again
# https://regex101.com/