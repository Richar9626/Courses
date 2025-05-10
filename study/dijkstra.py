import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with infinity and set the distance to the start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to hold nodes to explore
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest distance from the queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If a node's distance was updated and added to the priority queue again,
        # skip processing this (outdated) distance
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a new "shortest distance" is found for the neighbor, update and push it to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Return the final distances from the start node to all other nodes
    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")