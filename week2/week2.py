# Lecture code for Week 2
# inspired by https://www.programiz.com/python-programming/tuple

my_string = 'baldan'
type(my_string)

mystr1 = "Nice"
mystr2 = "day"

myFullStr = mystr1 + " " + mystr2

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

# tuple
my_tuple = (1,2,3)

# set
my_set1 = {1,2,3}
my_set2 = {7,8,9}
my_set.add(2)
my_set1 | my_set2 # join
my_set1 & my_set2 # intersection
my_set2 - my_set1


# dictionary . json

my_dict = {"name": "Bat", "age":25,"country":"Mongolia"}
person2 = {"name": "Bold", "age":23,"country":"Mongolia","city":"Darkhan"}

big_dict = {"Younger": person1, "Older": person2}


# Numerical package - numpy (scipy)

import numpy as np


# Pandas
import pandas as pd

# Pandas read examples:
# https://www.datacamp.com/community/tutorials/importing-data-into-pandas

# be careful with backward slash \
df = pd.read_excel("C:/Users/sugarkhuu/Documents/python/repo/Introduction_Python/week2/data.xlsx")
# pd.read_excel("C:\\Users\\sugarkhuu\\Documents\\python\\repo\\Introduction_Python\\week2\\data.xlsx")

df.dtypes
df.head()
df.tail()

df.describe()

df['age']
df['firstName']

# iloc
df.iloc[2,1]
df.iloc[2:5,1:3]

# loc
df.loc[5,"lastName"]
df.loc[5:8,"lastName"]
df.loc[5:8,("lastName","firstName")]

# filter
df[df["age"]<27]
df[df["age"]<27][["firstName","lastName","salary","age"]]
df[df["age"]>=27][["firstName","lastName","salary","age"]]


df[(df["age"]<27) & (df["salary"]<2.0) & (df["gender"] != "M")]


df.groupby('gender')['salary'].mean()
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()

df.groupby(['gender','politicalView'])['age'].mean()


df.groupby(['gender','politicalView'])['age'].mean()
df.groupby(['gender','politicalView'])[['age','salary']].mean()
df.groupby(['gender','politicalView'])[['age','salary']].max()

df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})

df.groupby(['gender','politicalView']).agg({'age': ["mean","max"], 'salary': ["max","count"]})

df.groupby(['gender','politicalView']).agg({'age': ["mean","max"],  \
    "salary": ["mean","max"] })


df = df.sort_values(by="yearsInCompany")

df.sort_values(by="gender", inplace=True)
df["name"] = np.arange(10)
del df["name"]

df[["age","salary"]]

df.columns # column names




