class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Avanzó {pasos} pasos. Posición actual: {self.posicion_x}")

    def abajo(self):
        print("Bajó una línea")

    def reiniciar(self):
        self.posicion_x = 0
        print("Posición reiniciada a 0")
