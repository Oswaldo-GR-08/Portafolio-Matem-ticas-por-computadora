import numpy as np
import matplotlib.pyplot as plt


# =========================================================================
# 1. DEFINICIÓN DEL SISTEMA DE ECUACIONES DIFERENCIALES ACOPLADAS
# =========================================================================
# Ecuación diferencial para la malla 1: di1/dt = -20*i1 + 10*i3 + 100
def di1_dt(t, i1, i3):
    return -20 * i1 + 10 * i3 + 100


# Ecuación diferencial para la malla 2: di3/dt = 10*i1 - 20*i3
def di3_dt(t, i1, i3):
    return 10 * i1 - 20 * i3


# =========================================================================
# 2. CONFIGURACIÓN DE PARÁMETROS DEL MÉTODO NUMÉRICO
# =========================================================================
h = 0.1  # Tamaño de paso (segundos)
t_inicial = 0.0  # Tiempo inicial
t_final = 5.0  # Tiempo final del análisis transitorio
pasos = int((t_final - t_inicial) / h)

# Arreglos de almacenamiento de datos inicializados en cero
t_val = np.zeros(pasos + 1)
i1_val = np.zeros(pasos + 1)
i3_val = np.zeros(pasos + 1)

# Condiciones iniciales (Circuito inicialmente desenergizado a t = 0)
t_val[0] = t_inicial
i1_val[0] = 0.0
i3_val[0] = 0.0

# =========================================================================
# 3. ALGORITMO DE RUNGE-KUTTA DE CUARTO ORDEN (RK4) MULTIVARIABLE
# =========================================================================
for n in range(pasos):
    t = t_val[n]
    i1 = i1_val[n]
    i3 = i3_val[n]

    # Pendientes iniciales del intervalo
    k1 = h * di1_dt(t, i1, i3)
    m1 = h * di3_dt(t, i1, i3)

    # Pendientes aproximadas en la mitad del intervalo usando k1 y m1
    k2 = h * di1_dt(t + h / 2, i1 + k1 / 2, i3 + m1 / 2)
    m2 = h * di3_dt(t + h / 2, i1 + k1 / 2, i3 + m1 / 2)

    # Pendientes refinadas en la mitad del intervalo usando k2 y m2
    k3 = h * di1_dt(t + h / 2, i1 + k2 / 2, i3 + m2 / 2)
    m3 = h * di3_dt(t + h / 2, i1 + k2 / 2, i3 + m2 / 2)

    # Pendientes al final del intervalo usando k3 y m3
    k4 = h * di1_dt(t + h, i1 + k3, i3 + m3)
    m4 = h * di3_dt(t + h, i1 + k3, i3 + m3)

    # Actualización del tiempo y cálculo de las ponderaciones RK4
    t_val[n + 1] = t + h
    i1_val[n + 1] = i1 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    i3_val[n + 1] = i3 + (m1 + 2 * m2 + 2 * m3 + m4) / 6

# =========================================================================
# 4. EXPORTACIÓN DE VALORES CALCULADOS A ARCHIVO DE TEXTO (.TXT)
# =========================================================================
# Esto te servirá para verificar los datos numéricos de tu tabla en LaTeX
with open("datos_corrientes_RK4.txt", "w") as f:
    f.write("Tiempo (s)\tCorriente i1 (A)\tCorriente i3 (A)\n")
    for idx in range(pasos + 1):
        f.write(f"{t_val[idx]:.1f}\t\t{i1_val[idx]:.4f}\t\t{i3_val[idx]:.4f}\n")

print("-> El archivo 'datos_corrientes_RK4.txt' se ha generado con éxito.")

# =========================================================================
# 5. GENERACIÓN Y CONFIGURACIÓN GRÁFICA DE LA SIMULACIÓN COMPUTACIONAL
# =========================================================================
plt.figure(figsize=(9, 5))

# Trazado de las curvas de corriente
plt.plot(t_val, i1_val, color='red', linewidth=2.0, label='Corriente $i_1(t)$ (Malla 1)')
plt.plot(t_val, i3_val, color='blue', linewidth=2.0, label='Corriente $i_3(t)$ (Malla 2)')

# Configuración de los ejes y formato del gráfico
plt.title('Respuesta Transitoria del Circuito RL Paralelo (Método RK4)', fontsize=13, fontweight='bold')
plt.xlabel('Tiempo $t$ (segundos)', fontsize=11)
plt.ylabel('Intensidad de Corriente $i$ (Amperios)', fontsize=11)

# Líneas guía de cuadrícula para facilitar la comparación analítica
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Colocación de la leyenda informativa y límites de visualización
plt.legend(loc='lower right', fontsize=10)
plt.xlim(-0.1, t_final + 0.1)
plt.ylim(-0.2, 7.5)

# Guardar la gráfica automáticamente con el nombre requerido para Overleaf
plt.savefig('WhatsApp Image 2026-05-18 at 3.20.59 PM.jpeg', dpi=300, bbox_inches='tight')
print("-> La gráfica se ha guardado como 'WhatsApp Image 2026-05-18 at 3.20.59 PM.jpeg'.")

# Mostrar la gráfica en pantalla
plt.show()