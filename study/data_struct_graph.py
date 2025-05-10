# Representación de un grafo mediante listas de adyacencia
   grafo = {
       'A': ['B', 'C'],
       'B': ['A', 'D'],
       'C': ['A', 'D', 'E'],
       'D': ['B', 'C', 'E'],
       'E': ['C', 'D']
   }

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

class graph_search:
    def __init__(self, graph):
        self.graph = graph

    def graph_display(self, start_node):
        current_node = start_node
        next_node = self.graph[start_node]
        while next_node != None:
            print("current node", current_node)
            for node in next_node:
                print("neighbor %s weight %s"%(node[0],node[1]))

            if len(next_node) <= 0:
                next_node = None
            else:
                current_node =  next_node[0][0]
                next_node = self.graph[current_node]

g_search = graph_search(graph)

g_search.graph_display("A")


class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not directed:
            self.graph[vertex2][vertex1] = weight

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"Vértice {vertex} tiene como conexiones a:")
            for neighbor, weight in edges.items():
                if weight:
                    print(f"  - {neighbor} (peso: {weight})")
                else:
                    print(f"  - {neighbor}")