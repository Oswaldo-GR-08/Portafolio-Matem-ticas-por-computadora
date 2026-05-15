import numpy as np

def resolver_newton_no_lineal():
    def F(v):
        x, y = v
        return np.array([
            x**2 + x*y - 10,
            y + 3*x*y**2 - 57
        ])

    def J(v):
        x, y = v
        return np.array([
            [2*x + y, x],
            [3*y**2, 1 + 6*x*y]
        ])

    def ejecutar_newton(x_start, tol=1e-8, max_iter=50):
        x_n = np.array(x_start, dtype=float)
        print(f"\n--- PROCESO PARA x0={x_start[0]}, y0={x_start[1]} ---")
        print(f"{'Iter':<5} | {'x':<12} | {'y':<12} | {'Error':<12}")
        print("-" * 55)
        
        for i in range(max_iter):
            F_n = F(x_n)
            J_n = J(x_n)
            
            delta = np.linalg.solve(J_n, -F_n)
            x_n = x_n + delta
            
            error = np.linalg.norm(delta)
            print(f"{i+1:<5} | {x_n[0]:<12.6f} | {x_n[1]:<12.6f} | {error:<12.2e}")
            
            if error < tol:
                return x_n
        return x_n

    print("RESOLUCION DE SISTEMA NO LINEAL")
    
    sol_1 = ejecutar_newton([1.5, 3.5])
    print(f"RESULTADO 1: x = {sol_1[0]:.8f}, y = {sol_1[1]:.8f}")

    sol_2 = ejecutar_newton([4.5, -2.5])
    print(f"RESULTADO 2: x = {sol_2[0]:.8f}, y = {sol_2[1]:.8f}")

if __name__ == "__main__":
    resolver_newton_no_lineal()