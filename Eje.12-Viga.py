# Autor: OGRI.
# Mi simulación numérica de deflexión para una Viga Cónica (Ejercicio 12)
import numpy as np
import matplotlib.pyplot as plt

def analizar_viga_conica(n_elementos=20, factor_delta=1.5):
    # 1. Configuro mis variables espaciales
    paso_h = 1.0 / n_elementos
    coord_xi = np.linspace(0, 1, n_elementos + 1)
    
    # 2. Ensamblaje de mi Matriz Tridiagonal principal
    tamano = n_elementos - 1
    Matriz_A = np.zeros((tamano, tamano))
    for fila in range(tamano):
        Matriz_A[fila, fila] = -2
        if fila > 0: Matriz_A[fila, fila - 1] = 1
        if fila < tamano - 1: Matriz_A[fila, fila + 1] = 1
            
    # 3. Función independiente que representa las cargas
    def carga_f(val_xi):
        return (1 - val_xi) / (1 + (factor_delta - 1) * val_xi)**4
    
    # Evalúo la carga únicamente en mis nodos interiores
    Vector_B = paso_h**2 * carga_f(coord_xi[1:-1])
    
    # 4. Solución del sistema de ecuaciones
    solucion_interna = np.linalg.solve(Matriz_A, Vector_B)
    perfil_y = np.concatenate(([0], solucion_interna, [0])) # Aseguro los apoyos en 0
    
    return coord_xi, perfil_y

# Corro la simulación
xi_nodos, deflexion_y = analizar_viga_conica()

# Grafico los resultados de mi análisis
plt.figure(figsize=(8, 5))
plt.plot(xi_nodos, deflexion_y, marker='^', color='darkred', linestyle='-.', label='Diferencias Finitas (m=20)')
plt.title('OGRI. - Análisis Estructural Viga Cónica')
plt.xlabel('Posición adimensional (xi)')
plt.ylabel('Deflexión calculada (y)')
plt.grid(True, linestyle=':')
plt.legend()
plt.show()