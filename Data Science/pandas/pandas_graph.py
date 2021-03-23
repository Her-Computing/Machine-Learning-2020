import pandas as pd
import matplotlib.pyplot as plt 
#reading in dataset using pandas
passengers = pd.read_csv('datasets/passengers.csv')

#getting x-coor by reading in dataset
x_coor = passengers['rank']
print(x_coor)

#getting y-coor by reading in dataset
y_coor = passengers['total_passengers']
print(y_coor)

#plotting graph using data
plt.plot(x_coor, y_coor)
plt.show()