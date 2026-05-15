import math

def punto_fijo(PO, TOL, i_max, funcion):
    def g(x):
        return eval(funcion)

    i = 1

    while i <= i_max:
        P = g(PO)

        print(f"Iteración {i}: P = {P}")

        if abs(P - PO) < TOL:
            print("\nProceso terminado con éxito :).")
            print("Raíz aproximada:", P)
            print("Hecho por Pao^^\n")
            return P

        PO = P
        i += 1

    print("Método fallido 🚫 No hecho correctamente")
    return None


# 🔁 LOOP PRINCIPAL
if _name_ == "_main_":
    while True:
        print(" MÉTODO DE PUNTO FIJO")

        funcion = input("Ingresa la funcion g(x): ")
        PO = float(input("Ingresar aproximacion inicial: "))
        TOL = float(input("Ingresar tolerancia: "))
        i_max = int(input("Ingresar numero maximo de iteraciones: "))

        punto_fijo(PO, TOL, i_max, funcion)

        opc = input("¿Deseas resolver otro problema? (s/n): ").lower()
        if opc != "s":
            print("\nPrograma finalizado. De Oswaldo Rdz^^")
            breakpo