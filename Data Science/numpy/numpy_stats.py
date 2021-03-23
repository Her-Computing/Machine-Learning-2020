import numpy as np 

#basic math functions
x = [-2, -1, 1, 2]

print("Absolute value: ", np.abs(x))
print("Exponential: ", np.exp(x)) #takes e to the power of elements of x
print("Logarithm: ", np.log(np.abs(x))) #takes log of abs value of elements of x

#aggregation

#sum all vals
nums = np.random.random(100)
totalSum = np.sum(nums) #sums up all values of nums
print(totalSum)

#sum of a column
cols = np.random.random((3,4))
print("\n", cols)
print("\n sum of all element in columns", cols.sum(axis = 0))
print("\n sum of all element in rows", cols.sum(axis = 1))

#basic statistics functions
print("\n", np.std(cols)) #mean standard deviation, how spread out data is from the average
print("\n",np.argmin(cols)) #prints index of the smallest element
print("\n", np.percentile(cols, 50))#prints number in 50 percentile