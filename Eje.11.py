# Autor: OGRI.
# Mi análisis de deflexión para la viga con inercias diferentes (Ejercicio 11)
import numpy as np
import matplotlib.pyplot as plt

def deflexion_viga_ej11(n_tramos=100):
    # Mis parámetros físicos de la viga
    L_total = 10.0
    Modulo_E = 200e9
    Inercia_A = 0.001
    Inercia_B = 0.002
    Carga_dist = 5000
    
    paso_h = (L_total / 2) / n_tramos
    distancia_x = np.linspace(0, L_total / 2, n_tramos + 1)
    
    # Inicializo mi sistema lineal (considerando la frontera de derivada al final)
    Matriz_K = np.zeros((n_tramos, n_tramos))
    Vector_F = np.zeros(n_tramos)
    
    # Lleno la matriz para todos los nodos interiores
    for nodo in range(1, n_tramos):
        idx = nodo - 1
        pos_x = distancia_x[nodo]
        
        # Componentes de la discretización de la segunda derivada
        if idx > 0: Matriz_K[idx, idx - 1] = 1
        Matriz_K[idx, idx] = -2
        if idx < n_tramos - 1: Matriz_K[idx, idx + 1] = 1
        
        # Defino mi función de momento f(x) dependiendo de en qué tramo estoy
        if pos_x <= L_total / 4:
            fuerza_x = (Carga_dist * L_total**2) / (4 * Modulo_E * Inercia_A) * (pos_x / L_total)
        else:
            fuerza_x = (Carga_dist * L_total**2) / (4 * Modulo_E * Inercia_B) * ((pos_x / L_total) - 2 * (pos_x / L_total - 0.25)**2)
        
        Vector_F[idx] = fuerza_x * paso_h**2

    # Agrego mi condición de frontera en el centro de la viga (pendiente nula)
    Matriz_K[n_tramos - 1, n_tramos - 2] = -1
    Matriz_K[n_tramos - 1, n_tramos - 1] = 1
    Vector_F[n_tramos - 1] = 0
    
    # Resuelvo el arreglo matricial
    desplazamientos_in = np.linalg.solve(Matriz_K, Vector_F)
    desplazamientos = np.concatenate(([0], desplazamientos_in)) # Agrego el empotramiento en 0
    
    return distancia_x, desplazamientos

# Proceso mis datos numéricos y genero la gráfica
x_ej11, v_ej11 = deflexion_viga_ej11()

plt.figure(figsize=(10, 4))
plt.plot(x_ej11, v_ej11, color='blue', linestyle='-', linewidth=2)
plt.title('OGRI. - Curva elástica de la viga (Ejercicio 11)')
plt.xlabel('Eje X (m)')
plt.ylabel('Deflexión V (m)')
plt.gca().invert_yaxis() # Invierto para visualizar la flexión real hacia abajo
plt.grid(True)
plt.show()