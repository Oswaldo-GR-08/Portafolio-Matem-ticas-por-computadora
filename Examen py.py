import math

def newtonRaphson(f, df, x0, i_max, tol=1e-8):
    x = x0
    k = 0
    cumple = False 

    print("{:^10s} {:^10s} {:^10s}".format("i", "x_i", "f(x_i)"))

    while (not cumple and k < i_max):
        if abs(df(x)) > tol:
            x = x - f(x)/df(x)
        else:
            x = x + tol

        print("{:10.5f} {:10.5f} {:10.5f}".format(x, f(x), df(x)))
        
        cumple = abs(f(x)) <= tol
        k += 1

    if cumple:
        return x
    else:
        raise ValueError("La función no converge")


def f(x):
    return x**3 - 1.2*x**2 - 8.19*x + 13.23

def df(x):
    return 3*x**2 - 1.4*x - 8.19       


raiz = newtonRaphson(f, df, x0=3, i_max=50)
print("Raíz aproximada:", raiz)

