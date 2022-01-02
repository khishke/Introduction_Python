# Loading files in general

import os
import sys

sys.path.append(r'D:\Documents\python\repo\Introduction_Python\4_Files\code')
from settings import *

# set main dir
# os.getcwd()
os.chdir(main_dir)


# GLOB
import glob

os.chdir(resource_dir) # switch to resource directory for ease of use
list_pdf = glob.glob('*.pdf')
glob.glob('khan*.pdf') # start with khan and end with .pdf
glob.glob('*k*.pdf')   # k somewhwere and end with .pdf
glob.glob('*.csv')     # end with .csv
glob.glob('*.png')     # end with .png
glob.glob('*.docx')    # end with .docx
glob.glob('*doc*')     # doc somewhere
glob.glob('*xlsx*')    # xlsx somewhere 

# looping through files with extension 'ext'
ext = 'pdf'
file_list = []
for filepath in glob.glob('*.' + ext):
    print(filepath)
    file_list.append(filepath)


# Conclusion
# https://www.programiz.com/python-programming/methods/built-in/open



f = open("anna.txt")      # equivalent to 'r' or 'rt'
f = open("anna.txt", mode='r')
f = open("anna.txt",'w')  # write in text mode
f.close()

file_name = 'anna_1.txt'
try:
   f = open(file_name)
   # perform file operations
except:
    print("No file named {}".format(file_name))
finally:
   f.close()
   
   
with open("anna.txt",'w', encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f.close()   
   
f = open("anna.txt",'w',encoding = 'utf-8')
f.read(4)    # read the first 4 data
f.read(4)    # read the next 4 data
f.read()     # read in the rest till end of file
f.tell()    # get the current file position
f.seek(0)   # bring file cursor to initial position
for line in f:
    print(line, end = '')


# # REcognize cyrillic Mongolian letters - utf-8-sig
# df = pd.read_excel('cyrillic.xlsx')
# df.to_csv('cyr.csv',encoding='utf-8-sig') # if cyrillic MNG is not recognized