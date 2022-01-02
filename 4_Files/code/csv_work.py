#%% Working with CSV files

#%% environment
import os
import sys

main_dir = r"D:\Documents\python\repo\Introduction_Python\4_Files"
sys.path.append(r'' + main_dir + '\code')
from settings import *


# set main dir
os.chdir(main_dir + '/' + resource_dir)

#%%
import csv

with open( 'data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
# append
with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["11", "Gerel", "Erdene"])
    writer.writerow(["12", "Gan", "Tuguldur"])
    writer.writerow(["13", "Chimeg", "Bayar"])
file.close()

# overwrite/write
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["11", "Gerel", "Erdene"])
    writer.writerow(["12", "Gan", "Tuguldur"])
    writer.writerow(["13", "Chimeg", "Bayar"])
file.close()


# don't open if exists - exclusive
with open('data.csv', 'x', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["11", "Gerel", "Erdene"])
    writer.writerow(["12", "Gan", "Tuguldur"])
    writer.writerow(["13", "Chimeg", "Bayar"])
file.close()


csv_rowlist = [["14", "Saran", "Khurel"], ["15", "Amar", "Khand"],
               ["16", "Tuvshin", "Tulga"]]

# write rows
with open('data.csv','a',newline='') as file: # , 
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

# write dictionary
with open('../' + result_dir + '/' + 'data_dict.csv', 'w', newline='') as file:
    fieldnames = ['id', 'firstName']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '17', 'firstName': 'Balbar'})
    writer.writerow({'id': '18', 'firstName': 'Ochir'})