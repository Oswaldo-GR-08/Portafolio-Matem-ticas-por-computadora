# Autor: OGRI.
# Implementación propia de diferencias finitas para una EDO de cuarto orden (Ejercicio 14)
import numpy as np

def solver_cuarto_orden(m_divisiones=20):
    tamano_h = 1.0 / m_divisiones
    
    # Inicializo mi matriz pentadiagonal
    dimension = m_divisiones - 1
    Matriz_Penta = np.zeros((dimension, dimension))
    Vector_Cargas = np.ones(dimension) # Asumo distribución de carga constante
    
    # Inserción de los coeficientes característicos para cuarto orden
    for idx in range(dimension):
        Matriz_Penta[idx, idx] = 6
        if idx > 0: Matriz_Penta[idx, idx - 1] = -4
        if idx < dimension - 1: Matriz_Penta[idx, idx + 1] = -4
        if idx > 1: Matriz_Penta[idx, idx - 2] = 1
        if idx < dimension - 2: Matriz_Penta[idx, idx + 2] = 1
            
    # Mis fronteras están simplificadas a cero, así que resuelvo directo
    desplazamientos_centrales = np.linalg.solve(Matriz_Penta / (tamano_h**4), Vector_Cargas)
    
    # Concateno las fronteras a mi resultado
    return np.concatenate(([0], desplazamientos_centrales, [0]))

print("OGRI. - Sistema de 4to orden evaluado y construido.")