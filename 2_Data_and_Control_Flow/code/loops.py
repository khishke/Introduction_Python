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

# Timing
a = np.arange(10000)
%timeit a + 1  

l = range(10000)
%timeit [i+1 for i in l] 

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