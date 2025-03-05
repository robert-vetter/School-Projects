from numpy import sin,linspace,power
from pylab import plot,show

def f(x): # sample function
 return x*sin(power(x,2))

# evaluation of the function
x = linspace(-2,4,150)
y = f(x)

a = 1.4
h = 0.1
fprime = (f(a+h)-f(a))/h # derivative
tan = f(a)+fprime*(x-a)  # tangent

# plot of the function and the tangent
plot(x,y,'b',a,f(a),'om',x,tan,'--r')
show()
