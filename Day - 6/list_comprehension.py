# List comprehension

# list comprehension is the way to defien a list with the help of loop and if conditions in the single way

# make a list of 1 to 20 numbers without list comprehension
mylist = []

for i in range(1,21):
    mylist.append(i)

print("\nmylist with list comprehension\n",mylist)

# make a list of 1 to 20 numbers with list comprehension
mySameList = [i for i in range(1,21)]
print("\nmySameList without list comprehension\n",mySameList)

print("\n")
# list of odd and even number between 1 to 50
odd = [i for i in range(1,51) if i%2 != 0]
even = [i for i in range(1,51) if i%2 == 0]
print("Odd = ", odd)
print("eve = ", even)


# make a new list which contains the square of ever element of list
list = [1,2,3,4,5]
squareList = [x*x for x in list]
print("\nList = ", list)
print("Square = ", squareList)


# make a new list which contains the all later of given string
str = "Hello World!"
charList = [j for j in str]
print("\nStr = ", str)
print("charList = ", charList)

