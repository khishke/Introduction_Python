print(x)   # global
res = my_func1() # shouldn't change the global
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
 
