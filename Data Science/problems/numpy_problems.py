'''
Problem:
Write a Python program to find the maximum and minimum value of a given array.
'''
print('Problem 1:')
print('----------------------------------------')

import numpy as np
a = np.arange(4).reshape((2,2)) #creates a blank 2 by 2 array
print("Original array:")
print(a)
print("Maximum value of the above array:")
print(np.amax(a))
print("Minimum value of the above array:")
print(np.amin(a))

'''
Problem: Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort the array on height.
'''
print('\nProblem 2:')
print('----------------------------------------')

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)   
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height')) 

'''
Problem: Write a NumPy program to sort the specified number of elements from least to greatest in an array
'''
print('\nProblem 3:')
print('----------------------------------------')

nums =  np.random.rand(10)
print("\nOriginal array:")
print(nums)
print("\nSorted entire array:")
print(nums[np.argpartition(nums,range(len(nums)))])