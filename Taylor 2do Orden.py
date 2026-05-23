# Autor: OGRI.
# Mi aproximación utilizando la Serie de Taylor de Orden 2
import math

# Defino la primera derivada (y') dada por el problema
def func_primera_derivada(x_val, y_val):
    return x_val**2 - 4 * y_val

# Defino la segunda derivada analítica (y'')
def func_segunda_derivada(x_val, y_val, y_prima):
    return 2 * x_val - 4 * y_prima

# Establezco mis condiciones iniciales y el tamaño de paso
x_actual = 0
y_actual = 1
tamano_paso = 0.05  # Requiero dos pasos iterativos para alcanzar 0.1

# Bucle principal de Taylor para dos iteraciones
for paso in range(2):
    y_p = func_primera_derivada(x_actual, y_actual)
    y_pp = func_segunda_derivada(x_actual, y_actual, y_p)
    
    # Aplico mi fórmula de expansión de Taylor
    y_actual = y_actual + (y_p * tamano_paso) + (y_pp * (tamano_paso**2)) / 2
    x_actual = x_actual + tamano_paso

print("El valor aproximado final que obtuve es:", y_actual)