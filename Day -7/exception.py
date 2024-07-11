# Exception Handeling

# exception is the one type of error which are generate at the run time 
# this run type error handeling is called as a exception handeling
# in python exception is handled by with the help of try and except block
# there are many types of errors like FileNotFound, NumberFormat etc.

try:
    
    no1 = 10
    no2 = "20"  

    ans = no1 + no2
except TypeError:

    print("Error is generate")

try:
    ans = 5/0
    print(x)
except ZeroDivisionError:
    print("Zero Division Error")

try:
    print(x)
except NameError:
    print("variable is not defined")
finally:
    # finally block is always execute if error is generate or not
    print("this is finally block")


try:
    with open("name.txt") as f:
        f.read()
except FileNotFoundError:
    print("File not found error")

try:
    list = [1,2,3]
    print(list[5])
except IndexError:
    print("Index Error")

# we can also rais user define exception

no = 2
if(no < 10):
    raise Exception("Only greater than 10 number is asscept")