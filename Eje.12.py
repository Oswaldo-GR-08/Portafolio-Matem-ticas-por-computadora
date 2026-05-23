# Autor: OGRI.
# Implementación de Taylor de Orden 5 para mi sistema de EDOs
import math

# Planteo mis condiciones iniciales
tiempo_t = 0
var_x = 1       # x(0)
var_x_prima = 2 # x'(0)
paso_iter = 0.1

# Listas donde almacenaré el histórico de mis derivadas
historico_d1 = [var_x]       # Derivadas correspondientes a x
historico_d2 = [var_x_prima] # Derivadas correspondientes a x'

# Defino la ecuación del problema analítico
def modelo_matematico(t_eval, x_eval, xp_eval):
    return (x_eval**2) * math.exp(t_eval) + xp_eval

# Calculo recursivamente las derivadas hasta alcanzar el 5to orden
for orden in range(5):
    if orden == 0:
        der_1 = var_x_prima
        der_2 = modelo_matematico(tiempo_t, var_x, var_x_prima)
    else:
        # Extraigo las derivadas previas para la regla de la cadena
        der_1 = historico_d2[orden] 
        der_2 = 2 * var_x * historico_d1[orden] * math.exp(tiempo_t) + (var_x**2) * math.exp(tiempo_t) + historico_d2[orden]
    
    # Guardo las evaluaciones actuales en mis arreglos
    historico_d1.append(der_1)
    historico_d2.append(der_2)

# Procedo a ensamblar la serie de Taylor final
aproximacion_taylor = 0
term_factorial = 1

for iterador in range(6):
    if iterador > 0:
        term_factorial *= iterador
    # Construyo el sumatorio característico de Taylor
    aproximacion_taylor += historico_d1[iterador] * (paso_iter**iterador) / term_factorial

print("Mi aproximación final estimada para x(0.1) es:", aproximacion_taylor)