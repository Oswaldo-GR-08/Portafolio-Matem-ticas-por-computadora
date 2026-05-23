# Autor: OGRI.
# Solución numérica para mi problema de valor en la frontera (Ejercicio 8)
import numpy as np

def resolver_frontera_ej8(n_intervalos=20):
    # Límites espaciales y condiciones de frontera
    lim_inf, lim_sup = 1, 2
    y_inicial, y_final = 0, 0.638961
    paso_espacial = (lim_sup - lim_inf) / n_intervalos
    vector_x = np.linspace(lim_inf, lim_sup, n_intervalos + 1)
    
    # Preparo mi matriz de coeficientes y el vector de cargas
    Matriz_Sistema = np.zeros((n_intervalos - 1, n_intervalos - 1))
    Vector_Resultados = np.zeros(n_intervalos - 1)
    
    # Construcción iterativa de la matriz tridiagonal
    for k in range(1, n_intervalos):
        val_x = vector_x[k]
        indice_matriz = k - 1
        
        # Genero los coeficientes usando diferencias finitas
        if indice_matriz > 0: 
            Matriz_Sistema[indice_matriz, indice_matriz - 1] = (val_x**2) / (paso_espacial**2) - val_x / (2 * paso_espacial)
        
        Matriz_Sistema[indice_matriz, indice_matriz] = -2 * (val_x**2) / (paso_espacial**2) + 1
        
        if indice_matriz < n_intervalos - 2: 
            Matriz_Sistema[indice_matriz, indice_matriz + 1] = (val_x**2) / (paso_espacial**2) + val_x / (2 * paso_espacial)

    # Resto mis condiciones de frontera en los extremos del vector
    Vector_Resultados[0] -= ((vector_x[1]**2) / (paso_espacial**2) - vector_x[1] / (2 * paso_espacial)) * y_inicial
    Vector_Resultados[-1] -= ((vector_x[-2]**2) / (paso_espacial**2) + vector_x[-2] / (2 * paso_espacial)) * y_final
    
    # Resuelvo el sistema para encontrar los puntos interiores
    nodos_internos = np.linalg.solve(Matriz_Sistema, Vector_Resultados)
    
    return vector_x, np.concatenate(([y_inicial], nodos_internos, [y_final]))

x_res8, y_res8 = resolver_frontera_ej8()
print(f"La evaluación específica en x=1.5 que obtuve es: {y_res8[10]:.4f}")