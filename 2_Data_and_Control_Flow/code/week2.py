# Lecture code for Week 2
# inspired by https://www.programiz.com/python-programming/tuple

my_string = 'baldan'
type(my_string)

mystr1 = "Nice"
mystr2 = "day"

myFullStr = mystr1 + mystr2 # myFullStr = mystr1 + " " + mystr2
print(myFullStr)

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


my_day = '2017-01-22'
my_dt = datetime.datetime.strptime(my_day, "%Y-%m-%d") # convert string to datetime (strptime)
my_day = '2017/01/22'
my_dt2 = datetime.datetime.strptime('2017/01/22', "%Y/%m/%d")

my_dt_str = today.strftime("%Y/%m/%d") # convert datetime to string (strptime)



# type conversion
# int(num_str)
# to_numeric
# to_datetime
# astype

# list
my_list_str = ['bat','bold','suren']
my_list_str[2]
my_list_str[:1]
my_list_str[:2]
my_list_str[1:]
my_list_str[::-1]
my_list_str[::-2]
my_list_str[-1]
my_list_str[-2]

my_list_num = [15, 15.2, 4.7]
type(my_list_num)

my_list_mix = [15, 15.2, 'hello']
type(my_list_mix)

# tuple
my_tuple = (1,2,3)

tuple(list(my_tuple))


# set
my_set1 = {1,2,3}
my_set2 = {1,2,7,8,9}
my_set1[2] # can not do this
my_set1.add(10)
my_set1.add(2)
my_set1.add(0)
my_set1.add(-5)

my_set1 | my_set2 # join
my_set1 & my_set2 # intersection
my_set2 - my_set1

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)
A.union(B)
B.union(A)

print(A & B)
A.intersection(B)
B.intersection(A)

print(A - B)
A.difference(B)
print(B - A)
B.difference(A)


# set additional 
my_set = {1,2,3}
my_set.update([2, 3, 4])
my_set.update([4, 5], {1, 6, 8})
my_set = {1, 3, 4, 5, 6}
my_set.discard(4) # no error if missing
my_set.remove(4)  # error if missing
my_set.remove(5)  # error if missing
my_set.pop() # drop first, show it on console



# dictionary . json

my_dict = {"name": "Bat", "age":25,"country":"Mongolia"}

my_dict['age'] 
my_dict.get('age')
my_dict['age'] = 27
my_dict['address'] = 'Downtown'

person2 = {"name": "Bold", "age":23,"country":"Mongolia","city":"Darkhan"}
big_dict = {"Younger": my_dict, "Older": person2}
big_dict['Younger']['name']


squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares.pop(4) # drop key with value 4
print(list(sorted(squares.keys())))
print(list(sorted(squares.values())))


# Numerical package - numpy (scipy) - Matrix operation important for Data science

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])   
print("3rd column =", column)


import numpy as np
a = np.array([1, 2, 3])
print(a)               # Output: [1, 2, 3]

my_zeros = np.zeros((2, 3))
my_zeros[0][2]
ones_array = np.ones( (4, 5), dtype=np.int32 ) 

ones_array = np.ones( (4,5,3), dtype=np.int32 ) 
ones_array[0][0]


A = np.arange(4)
B = np.arange(12).reshape(2, 6)
B = np.arange(12).reshape(3, 4)

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(A.transpose())

letters = np.array([1, 3, 5, 7, 9, 7, 5])

# just like list
print(letters[2:5]) 
print(letters[:-5])
print(letters[5:])
print(letters[:])
print(letters[::-1])
A[:,2]


a = np.array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = np.reshape(a,(7,5))
print(m)

m = np.reshape(a,(5,7))


# Pandas
import pandas as pd

# Pandas read examples:
# https://www.datacamp.com/community/tutorials/importing-data-into-pandas

# be careful with backward slash \

import os
os.getcwd()  

df = pd.read_excel(r"..\data\data.xlsx")

df.dtypes
df.head() # first 
df.tail() # last # df.tail(3)

df.describe() # descriptive statis

df['age']
df['firstName']

# iloc
df.iloc[2,1]
df.iloc[2:5,1:3]

# loc - index
df.loc[5,"lastName"]
df.loc[5:8,"lastName"]
df.loc[5:8,("lastName","firstName")]

df.set_index('firstName',drop=False, inplace=True) # , 
df.loc["Gerel","lastName"]


# filter
df[df["age"]<27]
df[~(df['age']<27)]['age']
df[df["age"]<27][["firstName","lastName","salary","age"]]
df[df["age"]>=27][["firstName","lastName","salary","age"]]


df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] != "M")]
df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] == "F")]

df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()

df.groupby(['gender','politicalView'])['age'].mean()


df.groupby(['gender','politicalView'])['age'].mean()
df.groupby(['gender','politicalView'])[['age','salary']].mean()
df.groupby(['gender','politicalView'])[['age','salary']].max()

# df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
res = df.groupby(['gender','politicalView']).agg({'age': ["mean","max"], 'salary': ["max","count"]})
len(res.columns)
res[('age','mean')]
res['age']


df.groupby(['gender','politicalView']).agg({'age': ["mean","max"], \
    "salary": ["mean","max"] })


df = df.sort_values(by="yearsInCompany")

df.sort_values(by="gender", inplace=True)
df["name"] = np.arange(10)
del df["name"]

df.reset_index(drop=True,inplace=True)

df[["age","salary"]]

df.columns # column names



# Control Flow
# https://www.programiz.com/python-programming/if-elif-else



# if
num = 3
if num > 0:
    print(num, "is a positive number.")

num = -3
if num > 0:
    print(num, "is a positive number.")


if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


### FOR

for i in range(15):
    print(i)

mylist = ['Bat','Geral','Bold']

for name in mylist:
    print(name)


for i in range(15):
    if i < 13: 
        if np.mod(i,2) == 0:
            print(i)
        else:
            print(i, ' Not even')
    else:
        break # skip the rest

for i in range(15):
    if (i > 8) and (i < 12): # &
        if np.mod(i,2) == 0:
            print(i)
        else:
            print(i, ' Not even')
    else:
        print(i, 'skipping')
        continue # skip this time


for i in range(15):
    if i > 10 : 
        print('passing')
        pass
    else:
        continue


mylist = [5,10,45,"Bold",45,45,'Chimeg']

for item in mylist:
    if isinstance(item, str):
        print(item)
        
for item in mylist:
    if isinstance(item, int):
        print(item)

                
for item in mylist:
    if type(item) == int:
        print(item)
        
short_list = [1,2,5]

for i in range(10):
    if i in short_list:
        print(i)


# WHILE


i = 1
while i>0:
    print(i)
    
i = 1    
while i < 100:
    print(i)
    i += 1 # i = i + 1
    
i = 1    
while i < 10:
    print(i)
    i *= 2
    
i = 10    
while i > 1:
    print(i)
    i /= 2


i = 10    
while i > 1:
    print(i)
    i -= 12