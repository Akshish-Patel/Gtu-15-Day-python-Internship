# Data Structure
# List
# Tuple
# Set
# Dictionaries

# list
# list can contains the more than 1 data into a single variable
# list is allows the duplicate data and maintain the insertation order
# list in mutable so we can change the value of list after once it declare
# list can contains the multiple type of data
# list is define by [] brackets

print("\n\nList")
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

print("\n\nTuple")
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

print("\n\nSet")
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

print("\n\nDictionary")
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

