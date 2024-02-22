from matplotlib.pyplot import *
from math import *
from numpy import *
tl=plot(80*sin(arange(-90,90,0.1 )),80*cos(arange(-90,90,0.1 )))
axis('scaled')
grid(True)
show()