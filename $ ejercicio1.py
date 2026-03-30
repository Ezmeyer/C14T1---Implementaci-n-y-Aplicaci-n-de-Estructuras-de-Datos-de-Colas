class Nodo:
    """
    Clase que representa un nodo de la lista enlazada.
    Cada nodo contiene un dato y una referencia al siguiente nodo.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """
    Implementación de una cola (FIFO) utilizando una lista enlazada.
    FIFO: First In, First Out -> El primer elemento en entrar es el primero en salir.
    """

    def __init__(self):
        self.frente = None  # Apunta al primer elemento de la cola
        self.final = None   # Apunta al último elemento de la cola
        self._tamano = 0    # Lleva el conteo de elementos en la cola

    def is_empty(self):
        """
        Retorna True si la cola está vacía, False en caso contrario.
        """
        return self.frente is None

    def enqueue(self, elemento):
        """
        Añade un elemento al final de la cola.
        """
        nuevo_nodo = Nodo(elemento)

        if self.is_empty():
            # Si la cola está vacía, el nuevo nodo será frente y final
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            # Si no está vacía, enlazamos el nuevo nodo al final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self._tamano += 1

    def dequeue(self):
        """
        Elimina y devuelve el elemento al frente de la cola.
        Lanza una excepción si la cola está vacía.
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")

        dato = self.frente.dato
        self.frente = self.frente.siguiente

        # Si después de eliminar el frente la cola queda vacía
        if self.frente is None:
            self.final = None

        self._tamano -= 1
        return dato

    def front(self):
        """
        Devuelve el elemento al frente de la cola sin eliminarlo.
        """
        if self.is_empty():
            raise IndexError("La cola está vacía")

        return self.frente.dato

    def size(self):
        """
        Retorna el número de elementos en la cola.
        """
        return self._tamano


# ---------------------------
# DEMOSTRACIÓN DE FUNCIONAMIENTO
# ---------------------------
if __name__ == "__main__":
    cola = Cola()

    print("¿La cola está vacía?", cola.is_empty())

    print("\nEncolando elementos: 10, 20, 30")
    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)

    print("Tamaño de la cola:", cola.size())
    print("Elemento al frente:", cola.front())

    print("\nDesencolando un elemento:", cola.dequeue())
    print("Nuevo frente:", cola.front())
    print("Tamaño actual:", cola.size())

    print("\nDesencolando todos los elementos restantes:")
    print(cola.dequeue())
    print(cola.dequeue())

    print("¿La cola está vacía ahora?", cola.is_empty())
