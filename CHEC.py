import math
import numpy as np
import matplotlib.pyplot as plt
 

def reglafalsa(f, x0, x1, tol=1e-8):
    if f(x0)*f(x1) > 0:
        raise ValueError ("La función no cambia de signo en este rango")
    sigue = False
    print("{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}" .\
    format("x0", "x", "x1", "f(x0)", "f(x)", "f(x1)"))
    while(not sigue):
        x = (x0*f(x1) - x1*f(x0)) / (f(x1) - f(x0))
        print("{:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f}".\
        format(x0, x, x1, f(x0), f(x), f(x1)))
        if f(x0)*f(x) < 0:
            x1 = x
        else:
            x0 = x
        sigue = abs(f(x)) < tol
    return x
def f(x):
    return -0.5*x**2+2.5*x+4.5
def main():
    #valores iniciales
    x0 = 6
    x1 = 7

    raiz = reglafalsa(f, x0, x1)
    print(raiz)

x=np.linspace(x0,x1,100)
y=f(x)
fig= plt.figure()
plt.plot (x,y)
plt.scatter(raiz,f(raiz))
plt.text(raiz,f(raiz), 'Raiz'+str(raiz),color='red')
plt.grid()

plt.show()

main()