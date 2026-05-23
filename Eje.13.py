# Autor: OGRI.
# Mi modelo para resolver un problema de frontera con condición mixta (Ejercicio 13)
import numpy as np

def resolver_condicion_mixta(num_nodos=20):
    paso_dx = 1.0 / num_nodos
    vector_espacial = np.linspace(0, 1, num_nodos + 1)
    
    # Defino mi espacio matricial
    Matriz_Coef = np.zeros((num_nodos, num_nodos))
    Vector_Term = np.zeros(num_nodos)
    
    # Asignación de coeficientes para la sección interior
    for iter_i in range(1, num_nodos):
        fila_real = iter_i - 1
        Matriz_Coef[fila_real, fila_real - 1] = 1 / (paso_dx**2)
        Matriz_Coef[fila_real, fila_real] = -2 / (paso_dx**2) + 9
        if fila_real < num_nodos - 2: 
            Matriz_Coef[fila_real, fila_real + 1] = 1 / (paso_dx**2)
            
    # Asigno mi condición de frontera en el extremo libre usando diferencia hacia atrás
    Matriz_Coef[num_nodos - 1, num_nodos - 3] = 1 / (2 * paso_dx)
    Matriz_Coef[num_nodos - 1, num_nodos - 2] = -4 / (2 * paso_dx)
    Matriz_Coef[num_nodos - 1, num_nodos - 1] = 3 / (2 * paso_dx)
    Vector_Term[num_nodos - 1] = 1
    
    # Ejecuto la resolución matemática
    solucion_numerica = np.linalg.solve(Matriz_Coef, Vector_Term)
    return vector_espacial, np.concatenate(([0], solucion_numerica))

# print("OGRI. - Ejercicio 13 procesado exitosamente.")