import numpy as np


# MATRIZ
A = np.array([[3, 6, 5, 6, 4,],
              [5, 9, 7, 8, 6],
              [6, 12, 13, 9, 7],
              [4, 6, 6, 5, 4],
              [2, 5, 4, 5, 3]], )
              
              
b = np.array([7/2, 14, -8, 23, -4], )

# Resolver el sistema Ax = b
x = np.linalg.solve(A, b) # "X" REPRESENTA LAS VARIABLES QUE DEBEMOS ENCONTRAR
#ESTA FORMULA SE UTILIZA PARA CUALQUIER ECUACION DE MATRICES QUE SE QUIERA RESOLVER

#"B" SON LAS VARIABLES INDEOENDIENTES DEL SISTEMA
#"A" ES LA MATRIZ ORIGINAL
print("La solución del sistema es:")
print(x)