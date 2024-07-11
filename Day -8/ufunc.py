import numpy as np

# ufuncs - universal functions
# universal functions are numpy functions which are perforn on the numpy array object

# numpy has many defined function but we can also create a ufuncs with the help of zip() mwthos

x = [1,2,3,4]
y = [4,5,6,7] 
z = []

for i,j in zip(x, y):
    z.append(i+j)

print("x = ",x)
print("y = ",y)
print("z = ",z)

# numpy has already add methos which is use to add the each element of the list to another list
print("\nadd() method")
x = [1,2,3,4]
y = [4,5,6,7] 
z = np.add(x, y)
print("x = ",x)
print("y = ",y)
print("z = ",z)


# creation of ufuncs

def addition(x,y):
    return x+y


addition = np.frompyfunc(addition, 2, 1)
#np.frompyfunc(func_name, no of input array, no of output array)

print("\nx = ",x)
print("y = ",y)
print("z = ",addition(x,y))


# simple arithmetic functions

x = [1,2,3,4,5]
y = [6,7,8,9,10]

print("\n\narithmetic functions\n\naddition")
x = np.add(x,y)  # add methos is use to add the each element of the list to another list
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

print("\nsubtract")
z = np.subtract(x,y) # # subtract methos is use to minus the each element of the list to another list
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

print("\multiplay")
z = np.multiply(x,y) # # multiplay methos is use to multiplay the each element of the list to another list
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

print("\division")
z = np.divide(x,y) # divide methos is use to divide the each element of the list to another list
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")


print("\power")
a = [1,2,3,4,5]
b = [1,2,3,4,5]
z = np.power(a,b) # power methos is use to powewr the each element of the list to another list
print(f"a = {a}")
print(f"b = {b}")
print(f"z = {z}")



