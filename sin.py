# Generating a sine vs cosine curve
# For this project, you will have a generate a sine vs cosine curve. You will need to use the numpy library to access the sine and cosine functions.
# You will also need to use the matplotlib library to draw the curve. To make this more difficult,
# make the graph go from -360� to 360�, with there being a 180� difference between each point on the x-axis.
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
sin = plt.plot(x, y)
cos = plt.plot(x, z)
plt.xticks(range(int(-2*3.14), int(2*3.14)+1))
plt.show()
