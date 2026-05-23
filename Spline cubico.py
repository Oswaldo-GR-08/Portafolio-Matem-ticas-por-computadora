# Autor: OGRI.
# Implementación propia para calcular los coeficientes 'c' de un Spline Cúbico Natural
import numpy as np

print("\n--- EJERCICIO 10 ---")

# Mis puntos de datos
x_nodos = np.array([0, 1, 2], dtype=float)
y_nodos = np.array([0, 2, 1], dtype=float)

def calcular_spline_natural(x_vals, y_vals):
    num_puntos = len(x_vals)
    
    # Calculo el paso entre cada par de nodos
    paso_h = np.diff(x_vals)

    # Configuro mi sistema de ecuaciones: Matriz_A * coef_c = vector_b
    Matriz_A = np.zeros((num_puntos, num_puntos))
    vector_b = np.zeros(num_puntos)

    # Aplico mis fronteras naturales (segunda derivada nula en los extremos)
    Matriz_A[0, 0] = 1
    Matriz_A[-1, -1] = 1

    # Ensamblaje de la matriz principal iterando sobre los nodos internos
    for idx in range(1, num_puntos - 1):
        Matriz_A[idx, idx - 1] = paso_h[idx - 1]
        Matriz_A[idx, idx] = 2 * (paso_h[idx - 1] + paso_h[idx])
        Matriz_A[idx, idx + 1] = paso_h[idx]
        
        # Defino los términos independientes
        termino_der = (y_vals[idx + 1] - y_vals[idx]) / paso_h[idx]
        termino_izq = (y_vals[idx] - y_vals[idx - 1]) / paso_h[idx - 1]
        vector_b[idx] = 3 * (termino_der - termino_izq)

    # Resuelvo el sistema lineal con numpy
    coeficientes_c = np.linalg.solve(Matriz_A, vector_b)
    return coeficientes_c

c_ej10 = calcular_spline_natural(x_nodos, y_nodos)
print("Mis coeficientes 'c' calculados son:", c_ej10)