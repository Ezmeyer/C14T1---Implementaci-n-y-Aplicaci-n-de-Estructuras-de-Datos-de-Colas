class Proceso:
    """
    Representa un proceso con un identificador y tiempo de ejecución restante.
    """
    def __init__(self, pid, tiempo):
        self.pid = pid
        self.tiempo = tiempo


class ColaCircular:
    """
    Implementación de una cola circular para simular Round Robin.
    """
    def __init__(self):
        self.cola = []

    def is_empty(self):
        return len(self.cola) == 0

    def enqueue(self, proceso):
        self.cola.append(proceso)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.cola.pop(0)

    def mostrar_cola(self):
        return [(p.pid, p.tiempo) for p in self.cola]

    def round_robin(self, quantum=3):
        """
        Simula la ejecución de procesos con algoritmo Round Robin.
        """
        while not self.is_empty():
            proceso = self.dequeue()
            print(f"Ejecutando Proceso {proceso.pid} por {quantum} unidades de tiempo")

            if proceso.tiempo > quantum:
                proceso.tiempo -= quantum
                print(f"Proceso {proceso.pid} no terminó, tiempo restante: {proceso.tiempo}")
                self.enqueue(proceso)
            else:
                print(f"Proceso {proceso.pid} finalizó su ejecución")

            print("Cola actual:", self.mostrar_cola())
            print("-" * 40)


# ---------------------------
# DEMOSTRACIÓN DE FUNCIONAMIENTO
# ---------------------------
if __name__ == "__main__":
    cola = ColaCircular()

    # Creación de 5 procesos con diferentes tiempos de ejecución
    cola.enqueue(Proceso("P1", 10))
    cola.enqueue(Proceso("P2", 4))
    cola.enqueue(Proceso("P3", 6))
    cola.enqueue(Proceso("P4", 8))
    cola.enqueue(Proceso("P5", 5))

    print("Cola inicial:", cola.mostrar_cola())
    print("Inicio de la simulación Round Robin ---")

    cola.round_robin(quantum=3)
