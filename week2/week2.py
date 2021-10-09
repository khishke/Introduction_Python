# Lecture code for Week 2
# inspired by https://www.programiz.com/python-programming/tuple

my_string = 'baldan'
type(my_string)

my_int = -15
type(my_int)

my_float = 15.78
type(my_float)

my_bool = False # True
type(my_bool)

import datetime 
today = datetime.date.today()
today.year
today.month
today.day

datetime.datetime.strptime('2017-01-22', "%Y-%m-%d") # convert string to datetime (strptime)
datetime.datetime.strptime('2017/01/22', "%Y/%m/%d")

today.strftime("%Y/%m/%d") # convert datetime to string (strptime)

