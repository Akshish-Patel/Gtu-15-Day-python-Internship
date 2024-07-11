import numpy as np

# creating array with the help of numpy library
array = np.array([1,2,3,4,5])
print("1-D Array")
print("array = ",array)
print("type of array = ",type(array))
print("dimension = ",array.ndim)

array2 = np.array([[1,2,3], [4,5,6]])
print("\n2-D Array")
print("array = \n",array2)
print("type of array = ",type(array2))
print("dimension = ",array2.ndim)

array3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print("\n3-D Array")
print("array = \n",array3)
print("type of array = ",type(array3))
print("dimension = ",array3.ndim)


# array indexing
print("\n\nArray Indexing")
array = np.array([1,2,3,4,5])
print("array = ",array)
print("array[3] = ",array[3]) #positive indexing is starting from the first element of the array and it's start from 0
print("array[-2] = ",array[-2]) # negative indexing is starting from the last element of the array and it's start from -1

array2 = np.array([[1,2,3], [4,5,6]])
print("\narray2 = ", array2)
print("array2[1][0] = ",array2[1][0]) 
print("array2[-1][-2] = ",array2[-1][-2])

array3 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print('\narray3 = ',array3)
print("array3[0][1][2] = ",array3[0][1][2])
print("array3[-1][-2][-3] = ",array3[-1][-2][-3])


# Array Slicing
# array slicing is the process of make a small part of array
print("\n\nArray Slicing")
array = np.array([1,2,3,4,5,6,7,8,9,10])
print("array = ",array)
print("array[0:4] = ", array[0:4]) #array[startIndex : EndIndex] pritn the element of array from index 0 to 3 
print("array[2:] = ", array[2:]) # print thr element of array from index 2 to all element
print("array[:5] = ", array[:5]) # print the element of array from index 0 to 4
print("array[-5:-1] = ",array[-5:-1]) # negative index printthe element of array from index -5(5) to -1(9)  
print("array[0::2] = ",array[0::2]) # print the elemet of array from index 0 to all with step 2 (step 2 means skip the 1 -1 element)

array2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print("\narray2 = ", array2)
print("arrar2[0:1 1:2] = ", array2[0:3, 1:4])


# numpy data types
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type

arr = np.array([1,2,3,4,5])
print("type of arr = ", arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


