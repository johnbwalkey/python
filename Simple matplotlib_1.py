import matplotlib
import numpy as np
import time

print(matplotlib.__version__)
time.sleep(3) # pause for 3 seconds

import matplotlib.pyplot as plt

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid()

plt.show()

# continue here -- https://www.w3schools.com/python/matplotlib_subplot.asp