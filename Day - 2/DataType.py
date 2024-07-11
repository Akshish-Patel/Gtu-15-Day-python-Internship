# This line is react as comment
# This is a single line Comment

"""
This line is react as a multi line comment
THis is a multi line comment
"""

# here x is called as a veriable which contains the '10' as a value
# python is case sensitive so tha small 'a' and capital 'A' both are different
x = 10
y = 20
name = "CKPCET"

print(f"x = {x}")
print(f"y = {y}")
print(f"Name = {name}")

# data types
# 1. int
# 2. float
# 3. string
# 4. boolean
# 5. list 
# 6. tuple
# 7. set 
# 8. dictionary 

# python can directly get the type of data we have not declare the type of data

# Integer
x = 10
print("Type of x is ", type(x))

# float
y = 3.4
print("Type of Y is ", type(y))

# string
a = "Hello World!!"
print("Type of a is ",type(a))

# boolean
b = False
print("Type of b is ", type(b))

# list
# list can contains the more than 1 data into a single variable
# list is allows the duplicate data and maintain the insertation order
# list in mutable so we can change the value of list after once it declare
# list can contains the multiple type of data
# list is define by [] brackets

myList = [1, 2, 3, 4, 5, 3, 2, 4]
print(myList)
print("Type of myList ", type(myList))

myList2 = [10, "ram", "shyam", 3.14, True]
print(myList2)
print("Type of myList2 ", type(myList2))

# tuple
# tuple can contains the more than 1 dara into a single variable
# tuple is allows the duplicate data and maintain the insertation order
# tuple is immutable so we can not change the value of tuple ones it declare
# tuple can contains the multiple types of data
# typle is define by () brackets

myTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(myTuple)
print("Type of myTuple ", type(myTuple))

myTuple2 = ("abc", 34, True, 40, "male")
print(myTuple2)
print("Type of myTuple ", type(myTuple2))

# set
# set can contains the more than 1 dara into a single variable
# set can not allows the duplicate data and dose not maintain the insertation order
# set is immutable so we can not change the value of tuple ones it declare
# set can contains the multiple types of data
# set is define by {} brackets

mySet =  {"apple", "banana", "cherry", True, 1, 2}
print(mySet)
print("Type of mySet ", type(mySet))

mySet2 = {"abc", 34, True, 40, "male"}
print(mySet2)
print("Type of mySet ", type(mySet2))

# dictionary
# dictionary can contains the more than 1 data into a single variable with key and value format
# dictionary can not allows the duplicate vakue of key and maintain the insertation order
# dictionary is mutable so we can change the value of dictionary ones it declare
# dictionary can contains the multiple types of data
# dictionary is define by {} brackets

myDesc = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(myDesc)
print("Type of myDesc ", type(myDesc))

myDesc2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(myDesc2)
print("Type of myDesc ", type(myDesc2))
