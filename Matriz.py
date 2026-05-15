import numpy as np

def resolver_matrices():
    # --- EJEMPLO 1: Matriz de la Tarea 2 (Inversa) ---
    print("--- EJEMPLO 1: MATRIZ TAREA 2 ---")
    A = np.array([
        [1, 2, 4, 3, 2],
        [1, 1, 3, 2, 3],
        [0, 2, 1, 3, 2],
        [0, 0, 1, 0, 3],
        [0, 0, 0, -1, -8]
    ], dtype=float)

    try:
        inv_A = np.linalg.inv(A)
        print("Matriz Inversa de A:")
        print(np.round(inv_A, 2)) # Redondeado a 2 decimales para claridad
    except np.linalg.LinAlgError:
        print("La matriz A no tiene inversa.")

    print("\n" + "="*40 + "\n")

    # --- EJEMPLO 2: Matriz del Sistema (Imagen 1) ---
    print("--- EJEMPLO 2: SISTEMA 5x5 ---")
    # Matriz de coeficientes
    B = np.array([
        [4, -2, -1, 1, 2],
        [1, 2, 2, -1, 4],
        [-2, -1, 4, -2, 2],
        [1, 1, 1, 1, 1],
        [6, 4, 1, -6, 6]
    ], dtype=float)

    # Vector de resultados (columna derecha de tu libreta)
    b_vector = np.array([14, 19, -8, 23, -4], dtype=float)

    try:
        # Resolver x = B^-1 * b
        x = np.linalg.solve(B, b_vector)
        print("Soluciones del sistema (x1, x2, x3, x4, x5):")
        for i, sol in enumerate(x, 1):
            print(f"x{i} = {round(sol, 4)}")
    except np.linalg.LinAlgError:
        print("El sistema no tiene solución única.")

if __name__ == "__main__":
    resolver_matrices()