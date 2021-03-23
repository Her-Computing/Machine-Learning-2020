#variables
print('Variable Basics')
print('----------------------------------------')

on_going_allowance = 500 #on_going_allowance is name, integer is type, value is 500
savings = 1000

#variable operations
savings = savings + 100
on_going_allowance = on_going_allowance - 50
number_of_days_to_save = (5000 - on_going_allowance) / 500
on_going_allowance = on_going_allowance + (30 - 10) * 7

print('Allowance', on_going_allowance)
print('Savings', savings)
print('Num Days', number_of_days_to_save)

print('Modulus', savings % 500) #mod
print('9 to the power 3', 9 ** 3) #raises 9 to the power 3

#advanced variable operations
savings += 100
savings = savings + 100
print('Savings', savings)

savings -= 100
savings = savings - 100
print('Savings', savings)

savings *= 100
savings = savings * 100
print('Savings', savings)

savings /= 100
savings = savings / 100
print('Savings', savings)

print('\nArrays')
print('----------------------------------------')
cars = ["Ford", "Volvo", "BMW", 3, 2.5]
print('First element', cars[0]) #printing first element of car array
print('Length of Array', len(cars)) #printing length of cars array

#editing Arrays
cars.append(3) #number three gets added to the end of the array
print('New Array', cars)

cars.pop(5) #deletes 6th element in array
print('Edited Array', cars)

cars.remove('Ford') #remove element with value ford
print('Edited Array version 2',cars)

#functions - example
#vacation_str is a parameter for function format_month_start
print('\nFunctions')
print('----------------------------------------')

def format_month_start(vacation_str):
  vacation_str_split = vacation_str.split(", ")
  vacation_str_iso = vacation_str_split[1]
  return vacation_str_iso

#calling function
vacation_str = "Milan, 6/15/2020"
print('Function output', format_month_start(vacation_str))

'''
Problem - Assignment: create a function that calculates the food an animal is going to need. Function should have 2 params: num_animals and food needed per animal. In order to calculate total food, the 2 params have to be multiplied together.

def calculate_food(num_animals, food):
  total_food = num_animals * food 
  return total_food

print('Total food needed', calculate_food(50, 3))
'''

