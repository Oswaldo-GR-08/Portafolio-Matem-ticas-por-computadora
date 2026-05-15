def punto_fijo(g, x0, i_max=50, tol=1e-8):
    x = x0
    k = 0
    cumple = False

    print("{:<5} {:<15} {:<15} {:<15}".format("k", "x_k", "x_k+1", "Error"))

    while not cumple and k < i_max:
        x_nuevo = g(x)
        error = abs(x_nuevo - x)

        print("{:<5} {:<15.10f} {:<15.10f} {:<15.10f}".format(k, x, x_nuevo, error))

        cumple = error < tol
        x = x_nuevo
        k += 1

    if cumple:
        return x
    else:
        raise ValueError("El método no converge")


def g(x):
    return x**4 - 3*x**2 - 3


# Valor inicial
x0 = 1

raiz = punto_fijo(g, x0)

print("\nRaíz aproximada:", raiz)
