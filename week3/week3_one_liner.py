import numpy as np

# one liner
# long
mlist = [] 
for i in range(10):
    print(i)
    mlist.append(i)
print(mlist)

# one line
mlist = [i for i in range(10)]    
print(mlist)

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

# long
if np.mod(i,2)==0:
    mlist.append(i)
else:
    mlist.append(i-1)

# short
# i if np.mod(i,2)==0 else i-1

status = False
xvar = 5 if status else 4

# lambda 

func = lambda a : a + 10
func(5)


def pos(input1):
    return True if input1 >0 else False

res = list(filter(pos,[1,-10,3,-7,4,-9]))

def neg(input1):
    return False if input1 >0 else True

res = list(filter(neg,[1,-10,3,-7,4,-9]))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# map
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

# zip
list1 = range(0,10)
list2 = range(10,20)

for i in zip(list1, list2):
    print(i)  

# enumerate  
for count, value in enumerate(list2):
    print(count, value)

# while loop
i = 1    
while i < 50:
    print(i)
    i += 1 # i = i + 150 i += 150

