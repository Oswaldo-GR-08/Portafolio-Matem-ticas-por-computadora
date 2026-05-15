import math

class BrazoRoboticoTerminal:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        # Ángulos en radianes
        self.q1 = 0.0
        self.q2 = 0.0

    def calcular_posiciones(self):
        """Calcula (x, y) usando cinemática directa."""
        # Eslabón 1
        x1 = self.l1 * math.cos(self.q1)
        y1 = self.l1 * math.sin(self.q1)
        # Eslabón 2 (Efector final)
        x2 = x1 + self.l2 * math.cos(self.q1 + self.q2)
        y2 = y1 + self.l2 * math.sin(self.q1 + self.q2)
        return (x1, y1), (x2, y2)

    def mostrar_jacobiano(self):
        """Calcula y muestra los componentes del Jacobiano analítico."""
        s1 = math.sin(self.q1)
        c1 = math.cos(self.q1)
        s12 = math.sin(self.q1 + self.q2)
        c12 = math.cos(self.q1 + self.q2)

        # J = [[dx/dq1, dx/dq2], [dy/dq1, dy/dq2]]
        j11 = -self.l1 * s1 - self.l2 * s12
        j12 = -self.l2 * s12
        j21 =  self.l1 * c1 + self.l2 * c12
        j22 =  self.l2 * c12

        print(f"\nMATRIZ JACOBIANA (J):")
        print(f"[{j11:8.3f}  {j12:8.3f}]")
        print(f"[{j21:8.3f}  {j22:8.3f}]")

    def dibujar_terminal(self):
        """Representación visual simple en la terminal."""
        (x1, y1), (x2, y2) = self.calcular_posiciones()
        print("\n" + "="*40)
        print(f"ESTADO DEL BRAZO (q1={math.degrees(self.q1):.1f}°, q2={math.degrees(self.q2):.1f}°)")
        print(f"Base: (0, 0) -> Codo: ({x1:.2f}, {y1:.2f}) -> Punta: ({x2:.2f}, {y2:.2f})")
        self.mostrar_jacobiano()
        print("="*40)

# --- PRUEBA DE FUNCIONAMIENTO ---

# Definimos longitudes l1=2.0, l2=1.5
robot = BrazoRoboticoTerminal(2.0, 1.5)

# Probamos las 3 posiciones que tienes en tu libreta
posiciones = [
    (0, 0),       # Posición 1: Extendida
    (90, 0),      # Posición 2: Vertical
    (0, 90)       # Posición 3: Codo doblado
]

for deg1, deg2 in posiciones:
    robot.q1 = math.radians(deg1)
    robot.q2 = math.radians(deg2)
    robot.dibujar_terminal()