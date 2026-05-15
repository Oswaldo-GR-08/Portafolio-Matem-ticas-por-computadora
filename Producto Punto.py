import numpy as np

np.set_printoptions(precision=3, suppress=True, floatmode='fixed')

# =============================
# EJERCICIO 1
# =============================
A1 = np.array([[1, 2, 3],
               [-1, 2, -3],
               [0, 1, 2]])

B1 = np.array([[1, 2],
               [0, 4],
               [-3, 2]])

R1 = np.dot(A1, B1)

print("Resultado Ejercicio 1:")
print(R1)

# =============================
# EJERCICIO 2
# =============================
A2 = np.array([[1, 2, 3],
               [4, 5, 6]])

B2 = np.array([[1, 2],
               [3, 4],
               [5, 6]])

R2 = np.dot(A2, B2)

print("\nResultado Ejercicio 2:")
print(R2)

# =============================
# EJERCICIO 3
# =============================
A3 = np.array([[1, 2],
               [3, 4]])

B3 = np.array([[5, 6],
               [7, 8]])

R3 = np.dot(A3, B3)

print("\nResultado Ejercicio 3:")
print(R3)

# =============================
# EJERCICIO 4 (Matriz Identidad)
# =============================
# Nota: En tu libreta mencionas que A4 es identidad, por eso R4 = B4
B4 = np.array([[2, 3, 4],
               [1, 0, 2],
               [3, 1, 5]])

# Creamos una identidad del mismo tamaño (3x3)
A4 = np.eye(3) 

R4 = np.dot(A4, B4)

print("\nResultado Ejercicio 4:")
print(R4)

# =============================
# EJERCICIO 5
# =============================
A5 = np.array([[1, 2, 3]]) # Vector fila

B5 = np.array([[4, 5],
               [6, 7],
               [8, 9]])

R5 = np.dot(A5, B5)

print("\nResultado Ejercicio 5:")
print(R5)