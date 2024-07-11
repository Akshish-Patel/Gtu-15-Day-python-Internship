# Function define

# in python function is define with the help of def key word
# def function_name (arguments):

#this is function define
def greet():
    # this function is use to print the "good mornign"
    print("Good morning!!")

# this is function calling
greet()

# there are 4 types of functions are there
# 1. with out argument and with out return type
# 2. with out argument and with return type
# 3. with  argument and with out return type
# 4. with argument and with return type


print("\n\nwith out argument and with out return type")
# 1. with out argument and with out return type
def addition():
     no1 = int(input("Enter the no1 : "))
     no2 = int(input("Enter the no2 : "))

     print(f"Addition of {no1} and {no2} is {no1+no2}")

# function calling
addition()

print("\n\nwith out argument and with return type")
# 2. with out argument and with return type
def subtraction():
     no1 = int(input("Enter the no1 : "))
     no2 = int(input("Enter the no2 : "))

     return no1-no2

print(f"Subtraction = {subtraction()}")

print("\n\nwith  argument and with out return type")
# 3. with  argument and with out return type
def multiplaction(no1, no2):
     
     print(f"Multiplaction of {no1} and {no2} is {no1*no2}")

no1 = int(input("Enter the no1 : "))
no2 = int(input("Enter the no2 : "))
multiplaction(no1, no2)

print("\n\nwith argument and with return type")
# 4. with argument and with return type
def division(no1, no2):
     return no1/no2
no1 = int(input("Enter the no1 : "))
no2 = int(input("Enter the no2 : "))
print(f"Multiplaction of {no1} and {no2} is {division(no1, no2)}")