#https://www.science-emergence.com/Articles/Calculer-et-tracer-la-d%C3%A9riv%C3%A9e-dune-fonction-avec-python/

from scipy import misc
from pylab import *

def fonction(x): 
    return x*x

value=misc.derivative(fonction, 2.0)
print(value)


ax = subplot(111)

def fonction(x):
    return 3*x*x+2*x+1

x = arange(-2.0, 2.0, 0.01)

y = fonction(x)

plot(x, y,'r-')

yp = misc.derivative(fonction, x)

plot(x, yp,'b-')

grid(True)

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

text(-0.75, 6.0,
     r'$f(x)=3x^2+2x+1$', horizontalalignment='center',
     fontsize=18,color='red')

text(-1.0, -8.0,
     r"$f'(x)=6x+2$", horizontalalignment='center',
     fontsize=18,color='blue')

show()
