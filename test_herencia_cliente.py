# cliente.py
from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, direccion, telefono):
        super().__init__(nombre, direccion)
        self.telefono = telefono

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente(nombre="Juan Pérez", direccion="Guayaquil", telefono="593908765432")
    print(f"Cliente 1: Teléfono: {cliente1.telefono}")