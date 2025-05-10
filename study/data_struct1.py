# Implementación simple de una lista enlazada
class Node:
      def __init__(self, data):
         self.data = data
         self.next = None

# Crear nodos
nodo1 = Node(1)
nodo2 = Node(2)
nodo3 = Node(3)
# Enlazar nodos
nodo1.next = nodo2
nodo2.next = nodo3
# Recorrer la lista
current = nodo1
while current:
      print(current.data)  # Output: 1, 2, 3
      current = current.next

#Stack
# Usando una lista como una pila
pila = []
pila.append(1)  # Agregar elemento
pila.append(2)
pila.append(3)
print(pila.pop())  # Output: 3 (último elemento agregado)

#queue
from collections import deque
# Usar deque para implementar una cola
cola = deque()
cola.append(1)  # Agregar elemento
cola.append(2)
cola.append(3)
print(cola.popleft())  # Output: 1 (primer elemento agregado)

#heap
import heapq
# Crear un min-heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
print(heapq.heappop(min_heap))  # Output: 1 (elemento más pequeño)