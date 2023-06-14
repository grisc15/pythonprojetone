import matplotlib.pyplot as plt
import numpy as np

t= np.linspace(-2*np.pi,2*np.pi,100)
def f(t):
    return (t+2*np.sin(2*t))
plt.plot(t,f(t),'*:k', ms=10)
plt.title('$x=t+2sin(2t)$\n$y=t+2sen(5t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')

def y(t):
    return (t+2*np.cos(5*t))
plt.plot(t,y(t),'*:y', ms =10)
plt.legend(['$f(x)$','$f(y)$'])
plt.grid(True)
plt.show()