import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000) #generates an array of 1000 numbers between 0 and 10
y = np.sin(x)

print(plt.style.available[:6])
# Change the size of the figure
fig = plt.figure(figsize=(12,8))
for i in range(6):    
  # This is how you add subplots
  fig.add_subplot(3,2,i+1)    
  plt.style.use(plt.style.available[i])    
  plt.plot(x, y)
  # This is how you write on a plot
  plt.text(s=plt.style.available[i], x=5, y=2, color='red')
  plt.show()

