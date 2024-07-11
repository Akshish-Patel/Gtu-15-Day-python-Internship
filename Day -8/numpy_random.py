import numpy as np
from numpy import random


# random.randin() function is give the random number between the given range
no = random.randint(100) # this randint(100) funtion is give the random no between 0 to 100
print("no = ",no)

no = random.rand() # rand() function is give the random no between 0 to 1 in float value
print("no = ",no)

no = random.randint(100, size=5) # this randint(100, size=5) funtion is give the list of 5 random int  no between 0 to 100
print(no)

no = random.randint(100, size=(2,3)) # this randint(100, size=(2,3)) funtion is give the 2-D array of (2,3) size random int  no between 0 to 100
print(no)

no = random.rand(5) # this rand(5) funtion is give the list of 5 random float no between 0 to 1
print(no)

# choice function

no = random.choice([2,4,6,8,10]) #choice([2,4,6,8,10]) function is give the random no from the given array[2,4,6,8,10]
print(no)

no = random.choice([1,3,5,7,9], size=3) # choice([1,3,5,7,9], size=3) function is give the list of 3 random no from the given array[1,3,5,7,9]
print(no)

no = random.choice([1,3,5,7,9], size=(2,3)) # choice([1,3,5,7,9], size=3) function is give the randonno of2-D array of size (2,3) from the given array[1,3,5,7,9]
print(no)

# Shuffling Arrays

print("\n\nShuffling Arrays")
arr = np.array([1,2,3,4,5])
print("Array befor shiffle method",arr) 
random.shuffle(arr) # shuffle method is randomly change arrangement of the array    
print("Array after shiffle method",arr) # shuffle method change the original array

print("\npermutation")
arr = np.array([1,2,3,4,5]) # permuration method is randomly change arrangement of the array    
random.permutation(arr) # permutation method is give the new changed array it can not change the original array
print(random.permutation(arr))