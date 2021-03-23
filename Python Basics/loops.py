print('Loops')
print('----------------------------------------')

#for loop
for x in range(5):
  print(x, end=' ')

#while loops
count = 0
print("\n")
while count < 5:
    print(count, end=' ')
    count += 1 

#break
print("\n")
count = 0
while True:
    print(count, end=' ')
    count += 1
    if count >= 5:
        #break exits loop if condition is met
        break

#continue
print("\n")
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        #continue skips over all even numbers
        continue
    print(x, end=' ')

'''
Problem - Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.
'''

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False 

    while not sorted:  
        sorted = True  

        for i in range(0, indexing_length): 
            if list_a[i] > list_a[i+1]:
                sorted = False 
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] 
    return list_a 

sorted_set = bubble(numbers)
print("\n\n\n", sorted_set)

print("\n\n\n\n")
for i in range(len(sorted_set)):
    if sorted_set[i] == 237:
        break

    if sorted_set[i] % 2 == 0:
        print(sorted_set[i], end=' ')


#class
print('\n\nClasses')
print('----------------------------------------')

class Person:
  #intializing parameter utilized throughout the class, in this case name
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    print("Hello my name is " + self.name)

#creating object of class person
p1 = Person("John")
p1.myfunc()