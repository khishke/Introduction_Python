# global scope
x = 20 # global by default

def my_func_lcl(ageby=5):
    
    x = 10+ageby
    return x

def my_func_glob(ageby=5):
    
    global x # use global variable inside a function
    x = x + ageby
    return x

print(x)   # global 
res = my_func_lcl() # should change the global
print(res) # x is changed inside the function
print(x)   # x is changed as global
 
 
print(x)   # global 
res = my_func_glob() # should change the global
print(res) # x is changed inside the function
print(x)   # x is changed as global