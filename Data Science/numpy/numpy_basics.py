import numpy as np
import random

def printLine():
  print("\n")

np.array([1, 2, 3, 4], dtype='float32') #generating basic numpy array, setting datatype manually

print(np.zeros(3)) #generates an array with three slots, all with value 0
printLine()

print(np.ones((4,5))) #generates 2-d array with 4 rows and 5 cols
printLine()

a = np.full((5,4), 3.14)
print("a shapte", a.shape)
print(np.full((5,4), 3.14))#generates 2-d array with 5 rows and 4 cols all values as 3.14
printLine()

#basic numy array stats

np.random.seed(0)
x1 = np.random.randint((10), size=6)  
# 1-dimensional array
print("Number of dimensions: ", x1.ndim)#number of dimensions
print("Shape: ", x1.shape)#num elements
print("Size: ", x1.size)#prints num of cols, rows
print("Type: ", x1.dtype) #what type of data is in array - only one type allowed


#accessing and editing array vals
edit = np.full((5,5), 3)
print(edit)
print(edit[0,1]) #prints val of number in first row, second col slot


edit[0,1] = 222.2 #edited value of number in first row, second col slot
printLine()
print(edit) #array cant hold .2 part b/c only data type in there is int right now

#concatenating arrays
printLine()
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y])) #result: 1 2 3 3 2 1 
print(x+ y)

#formatting arrays using vertical stacking
printLine()
x = np.array([1, 2, 3, 4])
grid = np.array([[9, 8, 7, 4], [6, 5, 4, 2]])
print(np.vstack([x, grid])) #prints array in rows of 3 because first array is in set of 3
printLine()

#formatting arrays using np.arange
print("A\n", np.arange(4).reshape(2, 2), "\n") #prints array with vals 0-3 
print("A\n", np.arange(4, 10, 2) ,"\n") #prints array with vals 4-9 incremented by 2


