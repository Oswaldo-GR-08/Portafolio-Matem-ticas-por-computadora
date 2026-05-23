# Autor: OGRI.
# Resolución de mi EDO utilizando métodos de Runge-Kutta (2do y 4to orden)
import math

# Ecuación diferencial principal a evaluar
def ec_diferencial(x_i, y_i):
    return x_i**2 - 4 * y_i

# Mis parámetros iniciales
x_inicial = 0
y_inicial = 1
paso_h = 0.1

# --- Implementación de Runge-Kutta Orden 2 ---
k_1_rk2 = ec_diferencial(x_inicial, y_inicial)
k_2_rk2 = ec_diferencial(x_inicial + paso_h, y_inicial + paso_h * k_1_rk2)

# Mi resultado de aproximación RK2
aprox_rk2 = y_inicial + (paso_h / 2) * (k_1_rk2 + k_2_rk2)
print("Mi resultado utilizando RK de orden 2 es:", aprox_rk2)


# --- Implementación de Runge-Kutta Orden 4 ---
k_1_rk4 = ec_diferencial(x_inicial, y_inicial)
k_2_rk4 = ec_diferencial(x_inicial + paso_h / 2, y_inicial + (paso_h / 2) * k_1_rk4)
k_3_rk4 = ec_diferencial(x_inicial + paso_h / 2, y_inicial + (paso_h / 2) * k_2_rk4)
k_4_rk4 = ec_diferencial(x_inicial + paso_h, y_inicial + paso_h * k_3_rk4)

# Mi resultado de aproximación RK4
aprox_rk4 = y_inicial + (paso_h / 6) * (k_1_rk4 + 2 * k_2_rk4 + 2 * k_3_rk4 + k_4_rk4)
print("Mi resultado utilizando RK de orden 4 es:", aprox_rk4)