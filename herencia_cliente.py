class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Cliente(Persona):
    def __init__(self, nombre, direccion, telefono):
        super().__init__(nombre, direccion)
        self.telefono = telefono

# Ejemplo de uso
cliente1 = Cliente(nombre="Juan Pérez", direccion="Guayaquil", telefono="593908765432")
print(f"Cliente 1: {cliente1.nombre}, Teléfono: {cliente1.telefono}")