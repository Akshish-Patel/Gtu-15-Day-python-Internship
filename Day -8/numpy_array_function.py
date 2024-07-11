import numpy as np

# array copy() function

arr1 = np.array([1,2,3,4])
arr2 = arr1.copy() # copy() function is use to make a clone of the arrar
arr1[0] = 10

print("\n\n copy()")
print("arr1 = ", arr1)
print("arr2 = ",arr2) # when we are use copy function it's create a new same array means if we are change the element of original array that effect can not reflect into the clone array

arr3 = arr1.view()
arr1[0] = 100

print("\n\n view()")
print("arr1 = ", arr1)
print("arr2 = ",arr3) # when we are use view function it's create a new same array means if we are change the element of original array that effect always reflect into the clone array

# array shape

# shape() functio is use to give the value of rows and colums of the array
print("\n\nShape()")
arr = np.array([1,2,3,4,5])
print("array = ",arr)
print("shape = ",arr.shape)

arr1 = np.array([[1,2,3], [4,5,6]])
print("\narr1 = ",arr1)
print("shape = ",arr1.shape)

arr3 = np.array([[[1,2,3], [1,2,3]], [[4,5,6], [4,5,6]]])
print("\narr3 = ",arr3)
print("shape = ",arr3.shape)


# reshape

# reshape() function is use to change the dimension of the array like 1-D to 2-D 

print("\n\nreshape()")
arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = arr1.reshape(3,3)
print("arr1 = ", arr1)
print("arr2 = ", arr2)

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr2 = arr1.reshape(9)
print("\narr1 = ", arr1)
print("arr2 = ", arr2)

# array iteration with the help of for loop

print("\n\narray iteration")
arr = np.array([1,2,3,4,5])
print("arr = ", arr)
for i in arr:
    print(i, end=" ")

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("\narr1 = ",arr1)

for i in arr1:
    for j in i:
        print(j,end=" ")

arr3 = np.array([[[1,2], [3,4]], [[5,6], [7,8]], [[9,10], [11,12]]])
print("\narr3 = ",arr3)

for i in arr3:
    for j in i:
        for k in j:
            print(k,end=" ")



print("\n\narray concatenate() function")
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
joinArry = np.concatenate((arr1, arr2))

print("1-D array concate")
print("arr1 = ",arr1)
print("arr2 = ",arr2)
print("joinArry = ",joinArry)

print("\n2-D array concate")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("arr1 = ",arr1)
print("arr2 = ",arr2)
print("axis = 1\n",arr) # if axis = 1 join array in row wise
arr = np.concatenate((arr1, arr2))
print("axis = 0\n",arr) #if axis = 0 join array in column wise


# stack() methods for array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\n\narr1 = ",arr1)
print("arr2 = ",arr2)
arr = np.hstack((arr1, arr2)) # hstack() function join the two array and make single 1-D array
print("hstack()\n",arr)
arr = np.vstack((arr1,arr2)) # vstach() function join the two array in vertical manner and make a single 2-D array
print("vstack()\n",arr)
arr = np.dstack((arr1,arr2)) # hstach() function join the two array in horizontal manner and make a single 2-D array (arr1[0] and arr2[0] join and create one row)
print("dstack()\n",arr)


# sort() function

print("\n\nsort()")
arr1 = np.array([6,3,8,2,9,1])
print("arr1 = ",arr1)
print("sorted arr = ",np.sort(arr1))

arr = np.array(['banana', 'cherry', 'apple'])
print("arr = ",arr)
print("sorted arr = ",np.sort(arr))