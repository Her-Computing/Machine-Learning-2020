import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000) #generates an array of 1000 numbers between 0 and 10

# Change default font size
plt.rcParams.update({'font.size': 15})

fig = plt.figure()
ax = plt.axes()

# Solid line, color specified by its name
plt.plot(x, np.sin(x - 0), color='blue', linestyle='solid', label='blue')
# Short name for color, dashed line
plt.plot(x, np.sin(x - 1), color='g', linestyle='dashed', label='green')
# Grayscale between 0 and 1, dashes and dots
plt.plot(x, np.sin(x - 1.75), color='red', linestyle='dashdot', label='gray')
# RGB color, dotted line
plt.plot(x, np.sin(x - 1.5), color='#FF0000', linestyle='dotted', label='red')
# Axis limits. Try also 'tight' and 'equal' to see their effect
plt.axis([-1, 11, -1.5, 1.5]);
# Labels
plt.title("Example of a graph")
# The legend is generated from the argument 'label' of 'plot'
# 'loc' specified the placement of the legend.
plt.legend(loc='lower right');
# Axis titles
ax = ax.set(xlabel='x', ylabel='sin(x)')

plt.show()


