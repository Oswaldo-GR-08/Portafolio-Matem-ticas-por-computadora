import numpy as np
np.set_printoptions(precision=3, suppress=True, floatmode='fixed')

# ==========================================
# EJERCICIO 1
# Definición de matrices
# ==========================================

M1 = np.array([[1, -2, 3],
               [2,  1, 4],
               [3, -1, -2]])

M2 = np.array([[0, 4, 2],
               [3, -1, -3]])

M3 = np.array([[-2, 1],
               [ 0,-1],
               [ 1, 3]])

M4 = np.array([[1, -3, 0],
               [2, -2, 2],
               [3, -1, 1]])

print("=== MATRICES INICIALES ===")
print("\nM1:\n", M1)
print("\nM2:\n", M2)
print("\nM3:\n", M3)
print("\nM4:\n", M4)


# ==========================================
# OPERACIONES
# ==========================================

print("\n=== OPERACIONES ===")

print("\nM1 + M4")
print(M1 + M4)

print("\nM4 - M1")
print(M4 - M1)

print("\n3 * M2")
print(3 * M2)

print("\nProducto elemento a elemento (M1 * M4)")
print(M1 * M4)

print("\nDivisión elemento a elemento (M1 / M4)")
print(M1 / M4)

print("\nMultiplicación matricial M1 @ M4")
print(M1 @ M4)

print("\nMultiplicación matricial M2 @ M3")
print(M2 @ M3)


# ==========================================
# EJERCICIO 2
# Inversa de matriz
# ==========================================

print("\n=== INVERSA ===")

inv_M1 = np.linalg.inv(M1)

print("\nM1:\n", M1)
print("\nM1^-1:\n", inv_M1)

print("\nVerificación (M1 @ M1^-1):")
print(M1 @ inv_M1)


# ==========================================
# EJERCICIO 3
# Clasificación de ecuaciones
# ==========================================

print("\n=== CLASIFICACIÓN ===")

lista = [
    "a) 2x - y = 7 -> Lineal",
    "b) 3x - 4 + 2z = 3y -> Lineal",
    "c) 4√x - 2y = 10 -> No lineal",
    "d) x/2 - 4y + z = 6 -> Lineal",
    "e) 3xy - 2y + z = 4 -> No lineal",
    "f) -x + 3y - sin(z) = 2 -> No lineal"
]

for eq in lista:
    print(eq)


# ==========================================
# EJERCICIO 4
# Sistema 2x2
# ==========================================

A_sys1 = np.array([[2, -1],
                   [3,  2]])

b_sys1 = np.array([5, 4])

print("\n=== SISTEMA 1 ===")
print(A_sys1)

res1 = np.linalg.solve(A_sys1, b_sys1)

print("Solución:")
print("x =", res1[0])
print("y =", res1[1])


# ==========================================
# EJERCICIO 5
# Sistema 4x4
# ==========================================

A_sys2 = np.array([[ 1, -3,  2, -1],
                   [ 2, -4,  5,  2],
                   [-1,  3, -1,  3],
                   [ 3,  2, -1, -1]])

b_sys2 = np.array([6, 13, -23, 6])

print("\n=== SISTEMA 2 ===")
print(A_sys2)

res2 = np.linalg.solve(A_sys2, b_sys2)

print("Solución:")
print("x =", res2[0])
print("y =", res2[1])
print("z =", res2[2])
print("w =", res2[3])


# ==========================================
# EJERCICIO 6
# Sistema 3x3
# ==========================================

A_sys3 = np.array([[ 1, -3,  2],
                   [ 2, -4,  5],
                   [-1,  3, -1]])

b_sys3 = np.array([6, 13, -23])

print("\n=== SISTEMA 3 ===")
print(A_sys3)

res3 = np.linalg.solve(A_sys3, b_sys3)

print("Solución:")
print("x =", res3[0])
print("y =", res3[1])
print("z =", res3[2])