import sys

def pos(input1):
    print("something")
    return True if input1 >0 else False

randomList = [5, 0, 2]

class myStrangeError(Exception):
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

a = 7

c = 5

e = 3

g = 12


pos(5)


for entry in randomList:
    try: 
        r = 1/int(entry)
        print(r)
    except:
        print("error. don't do conversion")


randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)



age = '30'

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass




    
