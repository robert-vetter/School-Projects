

from pylab import *

x = arange(-6.0, 4.0, 0.01)
y= x**3/4.0+3.0*x*x/4.0-3*x/2.0-2.0

ax = subplot(111)

ax.plot(x, y)

ax.scatter([-4,-1,2],[0,0,0])

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.set_xlim(-6,6)
ax.set_ylim(-20,20)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)


show()
