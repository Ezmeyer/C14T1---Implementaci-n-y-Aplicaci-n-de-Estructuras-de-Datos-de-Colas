class Paciente:
    """
    Representa un paciente con nombre y nivel de urgencia.
    1 es la mayor prioridad y 5 la menor.
    """
    def __init__(self, nombre, urgencia):
        self.nombre = nombre
        self.urgencia = urgencia


class ColaEmergencias:
    """
    Implementación de una cola de prioridad para atención hospitalaria.
    """
    def __init__(self):
        self.cola = []

    def is_empty(self):
        return len(self.cola) == 0

    def enqueue(self, paciente):
        """
        Inserta un paciente en la cola respetando el orden de prioridad.
        """
        self.cola.append(paciente)
        # Ordenamos por urgencia, manteniendo estabilidad para pacientes con igual prioridad
        self.cola.sort(key=lambda p: p.urgencia)

    def dequeue(self):
        """
        Atiende al paciente con mayor prioridad (menor número de urgencia).
        """
        if self.is_empty():
            raise IndexError("No hay pacientes en espera")
        return self.cola.pop(0)

    def mostrar_cola(self):
        """
        Muestra la lista actual de pacientes en espera.
        """
        return [(p.nombre, p.urgencia) for p in self.cola]


# ---------------------------
# DEMOSTRACIÓN DE FUNCIONAMIENTO
# ---------------------------
if __name__ == "__main__":
    cola = ColaEmergencias()

    # Se agregan al menos 8 pacientes con diferentes niveles de urgencia
    cola.enqueue(Paciente("Juan", 3))
    cola.enqueue(Paciente("María", 1))
    cola.enqueue(Paciente("Carlos", 4))
    cola.enqueue(Paciente("Ana", 2))
    cola.enqueue(Paciente("Luis", 5))
    cola.enqueue(Paciente("Elena", 1))
    cola.enqueue(Paciente("Pedro", 3))
    cola.enqueue(Paciente("Sofía", 2))

    print("Lista de espera inicial:")
    print(cola.mostrar_cola())

    print("--- Atendiendo pacientes ---")
    while not cola.is_empty():
        paciente = cola.dequeue()
        print(f"Atendiendo a {paciente.nombre} (urgencia {paciente.urgencia})")
        print("Pacientes restantes:", cola.mostrar_cola())
        print("-" * 40)
