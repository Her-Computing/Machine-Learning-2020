import matplotlib.pyplot as plt
import numpy as np

"""
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range, plt.errorbar(xCoord, yCoord, yerr = unsurePercent, fmt = ".k", ecolor= 'green', elinewidth = 3, capsize = 5); 
#error bar generates lines that extend from yCoord * 0.8 - Ycoord * 1.2 to show full range

Another aspect of plotting that we should be aware of is the degree of uncertainty associated with estimates. It is extremely important to take this into account not only when analyzing the data, but also when representing them. 
"""

plt.rcParams.update({'font.size' : 15})
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Graph of Sin(x) Errorbar")

#creating graph that shows error levels and certainity
xCoord = np.linspace(0, 10, 50)
unsurePercent = 0.2

yCoord = np.sin(xCoord) + unsurePercent * np.random.randn(50) #generates noisy sin curve b/c of unsure% times random num

plt.errorbar(xCoord, 
            yCoord, 
            xerr = unsurePercent, 
            yerr = unsurePercent, 
            fmt = ".k", 
            ecolor= 'green',  
            elinewidth = 3, 
            capsize = 5,
            )

plt.show()