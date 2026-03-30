class Cliente:
    """
    Representa un cliente del banco con nombre, tipo de servicio y prioridad.
    prioridad: 1 = alta (premium/adulto mayor), 2 = normal
    """
    def __init__(self, nombre, servicio, prioridad=2):
        self.nombre = nombre
        self.servicio = servicio  # 'caja', 'prestamos', 'consultas'
        self.prioridad = prioridad


class ColaSimple:
    """
    Cola FIFO básica para cada tipo de servicio.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


class ColaPrioridad:
    """
    Cola de prioridad que decide qué cliente se atiende primero
    entre todas las colas de servicio.
    """
    def __init__(self):
        self.cola = []

    def enqueue(self, cliente):
        self.cola.append(cliente)
        self.cola.sort(key=lambda c: c.prioridad)

    def dequeue(self):
        if self.cola:
            return self.cola.pop(0)
        return None

    def is_empty(self):
        return len(self.cola) == 0


class SistemaBanco:
    """
    Sistema que gestiona múltiples colas por servicio y una cola de prioridad global.
    """
    def __init__(self):
        self.cajas = ColaSimple()
        self.prestamos = ColaSimple()
        self.consultas = ColaSimple()
        self.prioridades = ColaPrioridad()

    def llegar_cliente(self, cliente):
        """
        Registra la llegada de un cliente al sistema.
        """
        # Se añade a la cola de su servicio
        if cliente.servicio == 'caja':
            self.cajas.enqueue(cliente)
        elif cliente.servicio == 'prestamos':
            self.prestamos.enqueue(cliente)
        elif cliente.servicio == 'consultas':
            self.consultas.enqueue(cliente)

        # También se añade a la cola de prioridad global
        self.prioridades.enqueue(cliente)

    def atender_cliente(self):
        """
        Atiende al siguiente cliente según prioridad y servicio.
        """
        cliente = self.prioridades.dequeue()
        if cliente is None:
            print("No hay clientes en espera.")
            return

        # Se elimina también de la cola específica del servicio
        if cliente.servicio == 'caja':
            self.cajas.dequeue()
        elif cliente.servicio == 'prestamos':
            self.prestamos.dequeue()
        elif cliente.servicio == 'consultas':
            self.consultas.dequeue()

        print(f"Atendiendo a {cliente.nombre} en {cliente.servicio} (prioridad {cliente.prioridad})")

    def mostrar_estado(self):
        """
        Muestra el estado actual de todas las colas.
        """
        print("Caja:", [c.nombre for c in self.cajas.items])
        print("Préstamos:", [c.nombre for c in self.prestamos.items])
        print("Consultas:", [c.nombre for c in self.consultas.items])


# ---------------------------
# DEMOSTRACIÓN DE FUNCIONAMIENTO
# ---------------------------
if __name__ == "__main__":
    banco = SistemaBanco()

    # Llegada de clientes
    banco.llegar_cliente(Cliente("Ana", "caja", 2))
    banco.llegar_cliente(Cliente("Luis", "prestamos", 1))
    banco.llegar_cliente(Cliente("María", "consultas", 2))
    banco.llegar_cliente(Cliente("Pedro", "caja", 1))
    banco.llegar_cliente(Cliente("Sofía", "consultas", 2))
    banco.llegar_cliente(Cliente("Carlos", "prestamos", 2))

    print("Estado inicial de las colas:")
    banco.mostrar_estado()

    print("--- Atención de clientes ---")
    for _ in range(6):
        banco.atender_cliente()
        banco.mostrar_estado()
        print("-" * 40)
