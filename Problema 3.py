import numpy as np

def determinarCircunferencia(x, y):
    A = np.array([
        [2*x[0], 2*y[0], 1],
        [2*x[1], 2*y[1], 1],
        [2*x[2], 2*y[2], 1]
    ])
    
    B = np.array([
        [x[0]**2 + y[0]**2],
        [x[1]**2 + y[1]**2],
        [x[2]**2 + y[2]**2]
    ])

    try:
        sol = np.linalg.solve(A, B)
        a = sol[0][0]
        b = sol[1][0]
        c = sol[2][0]
        
        radio = np.sqrt(c + a**2 + b**2)
        
        print("{:^10s} {:^15s}".format("Parámetro", "Valor"))
        print("-" * 25)
        print("{:^10s} {:15.5f}".format("Centro a", a))
        print("{:^10s} {:15.5f}".format("Centro b", b))
        print("{:^10s} {:15.5f}".format("Radio R", radio))
        
        return a, b, radio
    except np.linalg.LinAlgError:
        raise ValueError("Los puntos están alineados, no forman un círculo")

x_coords = [-2.2047, 4.7297, 3.5377]
y_coords = [5.2202, 1.2313, 6.5454]

a, b, R = determinarCircunferencia(x_coords, y_coords)