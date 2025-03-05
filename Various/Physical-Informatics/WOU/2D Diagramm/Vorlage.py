import matplotlib.pyplot as plt
import numpy as np

xwerte = [0, 1, 2, 3, 4, 5]
ywerte = [4, 7, 5, 3, 9, 5]

plt.plot(xwerte, ywerte)
plt.scatter(xwerte, ywerte)
plt.xlabel("x-Werte")
plt.ylabel("y-Werte")
plt.xlim([0, 5])
plt.ylim([3, 9])
plt.show()
